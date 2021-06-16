from django.shortcuts import render
from django.views import generic

from producto.models import Categoria, Producto

# Create your views here.

class Home(generic.TemplateView):
  template_name = 'store/home.html'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context["productos"] = Producto.objects.filter(is_disponible=True)[:10]
    context["categorias"] = Categoria.objects.all()
    return context

class About(generic.TemplateView):
  template_name = 'store/about.html'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context["categorias"] = Categoria.objects.all()
    return context

class Categorias(generic.TemplateView):
  template_name = 'store/categorias.html'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context["categorias"] = Categoria.objects.all()
    return context

class NuevoProducto(generic.TemplateView):
  template_name = 'store/nuevo_producto.html'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context["categorias"] = Categoria.objects.all()
    return context

class Carrito(generic.TemplateView):
  template_name = 'store/carrito.html'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context["categorias"] = Categoria.objects.all()
    return context

