from django.urls import path
from .views import ProductoDetailView, ProductoListView


urlpatterns = [
  path("", ProductoListView.as_view(), name="lista"),
  path("<slug:slug>/", ProductoDetailView.as_view(), name="detalle"),
  path("categoria/<slug:slug>/", ProductoListView.as_view(), name="lista_por_categoria"),
]
