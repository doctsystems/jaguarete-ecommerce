import copy
from decimal import Decimal
from django.conf import settings
from producto.models import Producto
from .forms import CartAddProductoForm


class Cart:

  def __init__(self, request):
    if request.session.get(settings.CART_SESSION_ID) is None:
      request.session[settings.CART_SESSION_ID] = {}

    self.cart = request.session[settings.CART_SESSION_ID]
    self.session = request.session

  def __iter__(self):
    cart = copy.deepcopy(self.cart)

    productos = Producto.objects.filter(id__in=cart)
    for producto in productos:
      cart[str(producto.id)]["producto"] = producto

    for item in cart.values():
      item["precio"] = Decimal(item["precio"])
      item["precio_total"] = item["cantidad"] * item["precio"]
      item["update_cantidad_form"] = CartAddProductoForm(
        initial={
          "cantidad": item["cantidad"],
          "override": True
        }
      )
      yield item

  def __len__(self):
    return sum(item["cantidad"] for item in self.cart.values())

  def add(self, producto, cantidad=1, override_cantidad=False):
    producto_id = str(producto.id)

    if producto_id not in self.cart:
      self.cart[producto_id] = {
        "cantidad": 0,
        "precio": str(producto.precio),
      }

    if override_cantidad:
      self.cart[producto_id]["cantidad"] = cantidad
    else:
      self.cart[producto_id]["cantidad"] += cantidad

    self.cart[producto_id]["cantidad"] = min(10, self.cart[producto_id]["cantidad"])

    self.save()

  def remove(self, producto):
    producto_id = str(producto.id)

    if producto_id in self.cart:
      del self.cart[producto_id]
      self.save()

  def get_precio_total(self):
    return sum(Decimal(item["precio"]) * item["cantidad"] for item in self.cart.values())

  def clear(self):
    del self.session[settings.CART_SESSION_ID]
    self.save()

  def save(self):
    self.session.modified = True
