from .models import Producto, Categoria


def products(request):
  return {
    'productos': Producto.objects.filter(is_disponible=True)[:10],
  }


def categories(request):
  return {
    'categories': Categoria.objects.all()
  }
