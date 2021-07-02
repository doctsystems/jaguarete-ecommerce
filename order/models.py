from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from model_utils.models import TimeStampedModel
from producto.models import Producto


class Order(TimeStampedModel):
  nombre = models.CharField("Nombre completo", max_length=250)
  email = models.EmailField()
  direccion = models.CharField("Direccion", max_length=250)
  numero = models.CharField("Número", max_length=250)
  descripcion = models.CharField("Descripcion", max_length=250, blank=True)
  ciudad = models.CharField("Ciudad", max_length=250)
  is_pagado = models.BooleanField(default=False)

  class Meta:
    ordering = ("-created", )
    verbose_name = "Orden"
    verbose_name_plural = "Ordenes"

  def __str__(self):
    return 'Pedido {}'.format(self.id)

  def get_precio_total(self):
    total_costo = sum(item.get_precio_total() for item in self.items.all())
    return total_costo

  def get_description(self):
    return ", ".join(
      [
        '{} x {}'.format(item.cantidad, item.producto.nombre) for item in self.items.all()
      ]
    )


class Item(models.Model):
  orden = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE)
  producto = models.ForeignKey(
    Producto, related_name="order_items", on_delete=models.CASCADE
  )
  precio = models.DecimalField(max_digits=10, decimal_places=2)
  cantidad = models.PositiveIntegerField(
    validators=[
      MinValueValidator(1),
      MaxValueValidator(settings.CART_ITEM_MAX_CANTIDAD),
    ]
  )

  def __str__(self):
    return str(self.id)

  def get_precio_total(self):
    return self.precio * self.cantidad
