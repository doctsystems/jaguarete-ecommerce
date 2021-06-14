from django.shortcuts import render
from django.views import generic

# Create your views here.

class Home(generic.TemplateView):
  template_name = 'store/home.html'

class About(generic.TemplateView):
  template_name = 'store/about.html'

class Categorias(generic.TemplateView):
  template_name = 'store/categorias.html'

class NuevoProducto(generic.TemplateView):
  template_name = 'store/nuevo_producto.html'

class Carrito(generic.TemplateView):
  template_name = 'store/carrito.html'

