from django.urls import path

from .views import ProductoDetailView, ProductoListView

app_name = "productos"

urlpatterns = [
  path("", ProductoListView.as_view(), name="lista_productos"),
  path("<slug:slug>/", ProductoDetailView.as_view(), name="detalle_producto"),
  path("categoria/<slug:slug>/", ProductoListView.as_view(), name="lista_por_categoria"),
]
