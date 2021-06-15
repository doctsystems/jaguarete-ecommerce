from django.contrib import admin
from .models import Categoria, Producto


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
  list_display = ["nombre", "slug", "created", "modified"]


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
  list_display = [
    "nombre",
    "slug",
    "categoria",
    "precio",
    "is_disponible",
    "created",
    "modified",
  ]
  list_filter = ["is_disponible", "created", "modified"]
  list_editable = ["precio", "is_disponible"]
