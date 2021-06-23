from django.urls import path
from .views import *

urlpatterns = [
  path("", ProductoListView.as_view(), name="lista"),
  path("nuevo/", ProductoCreateView.as_view(), name="nuevo"),
  path("actualizar/<slug:slug>/", ProductoUpdateView.as_view(), name="actualizar"),
  path("eliminar/<slug:slug>/", ProductoDeleteView.as_view(), name="eliminar"),
  path("<slug:slug>/", ProductoDetailView.as_view(), name="detalle"),
  path("categoria/<slug:slug>/", ProductoListView.as_view(), name="lista_por_categoria"),
  path("buscar/<str:filter>/", ProductoListView.as_view(), name="buscar"),
]
