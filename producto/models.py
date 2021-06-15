from autoslug import AutoSlugField
from django.db import models
from django.urls import reverse
from model_utils.models import TimeStampedModel


class Categoria(TimeStampedModel):
  nombre = models.CharField(max_length=255, unique=True, help_text="Nombre de categoria")
  slug = AutoSlugField(unique=True, always_update=False, populate_from="nombre")

  class Meta:
    ordering = ("nombre", )
    verbose_name = "Categoria"
    verbose_name_plural = "Categorias"

  def __str__(self):
    return self.nombre

  def save(self):
    self.nombre=self.nombre.upper()
    super(Categoria, self).save()

  def get_absolute_url(self):
    return reverse("productos:lista_por_categoria", kwargs={"slug": self.slug})


class Producto(TimeStampedModel):
  categoria = models.ForeignKey(
    Categoria, related_name="productos", on_delete=models.CASCADE
  )
  nombre = models.CharField(max_length=50, unique=True, help_text="Nombre de producto")
  slug = AutoSlugField(unique=True, always_update=False, populate_from="nombre")
  imagen = models.ImageField(upload_to="img/productos/%Y/%m/%d", blank=True, null=True)
  descripcion = models.TextField()
  precio = models.DecimalField(max_digits=10, decimal_places=2)
  is_disponible = models.BooleanField(default=True)

  class Meta:
    ordering = ("-id", )

  def __str__(self):
    return self.nombre

  def save(self):
    self.nombre=self.nombre.upper()
    super(Producto, self).save()

  def get_absolute_url(self):
    return reverse("productos:detalle_producto", kwargs={"slug": self.slug})
