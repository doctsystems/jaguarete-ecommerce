from django.urls import path

from .views import cart_add, cart_detalle, cart_eliminar


urlpatterns = [
  path("", cart_detalle, name="detalle"),
  path("add/<int:producto_id>/", cart_add, name="add"),
  path("eliminar/<int:producto_id>/", cart_eliminar, name="eliminar"),
]
