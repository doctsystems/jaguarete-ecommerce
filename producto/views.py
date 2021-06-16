from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView
from cart.forms import CartAddProductoForm
from .models import Categoria, Producto


class ProductoDetailView(DetailView):
  queryset = Producto.objects.filter(is_disponible=True)
  extra_context = {"form": CartAddProductoForm()}

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context["categorias"] = Categoria.objects.all()
    return context


class ProductoListView(ListView):
  categoria = None
  paginate_by = 3

  def get_queryset(self):
    queryset = Producto.objects.filter(is_disponible=True)

    categoria_slug = self.kwargs.get("slug")
    if categoria_slug:
      self.categoria = get_object_or_404(Categoria, slug=categoria_slug)
      queryset = queryset.filter(categoria=self.categoria)

    return queryset

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context["categoria"] = self.categoria
    context["categorias"] = Categoria.objects.all()
    return context
