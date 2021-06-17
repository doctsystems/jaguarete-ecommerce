from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from producto.models import Producto, Categoria

from .cart import Cart
from .forms import CartAddProductoForm


@require_POST
def cart_add(request, producto_id):
  cart = Cart(request)
  producto = get_object_or_404(Producto, id=producto_id)

  form = CartAddProductoForm(request.POST)
  if form.is_valid():
    cart_add = form.cleaned_data
    cart.add(producto=producto, cantidad=cart_add["cantidad"], override_cantidad=cart_add["override"])

  return redirect("cart:detalle")


@require_POST
def cart_eliminar(request, producto_id):
  cart = Cart(request)
  producto = get_object_or_404(Producto, id=producto_id)
  cart.remove(producto)
  return redirect("cart:detalle")


def cart_detalle(request):
  cart = Cart(request)
  categorias = Categoria.objects.all()
  return render(request, "cart/cart_detail.html", {"cart": cart, "categorias": categorias})
