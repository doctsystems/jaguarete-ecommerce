from django.urls import path
from .views import Home, About, Categorias, NuevoProducto, Carrito


urlpatterns = [
	path('', Home.as_view(), name='home'),
	path('about/', About.as_view(), name='about'),
	path('nuevo/', NuevoProducto.as_view(), name='nuevo_producto'),
]