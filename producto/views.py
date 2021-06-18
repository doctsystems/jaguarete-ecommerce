from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from cart.forms import CartAddProductoForm
from .models import Categoria, Producto
from .forms import ProductoForm


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


class ProductoCreateView(CreateView):
  model = Producto
  template_name = 'producto/producto_create.html'
  form_class = ProductoForm
  success_url = reverse_lazy('producto:lista')
  # permission_required = 'add_persona'

  def post(self, request, *args, **kwargs):
    form = ProductoForm(request.POST, request.FILES)
    if form.is_valid():
      form.save()
      return HttpResponseRedirect(self.success_url)
    self.object = None
    context = self.get_context_data(**kwargs)
    context['categorias'] = Categoria.objects.all()
    context['form'] = form
    return render(request, self.template_name, context)

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['categorias'] = Categoria.objects.all()
    return context


class ProductoUpdateView(UpdateView):
  model = Producto
  form_class = ProductoForm
  template_name = 'producto/producto_update.html'
  success_url = reverse_lazy('producto:lista')

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['categorias'] = Categoria.objects.all()
    return context


class ProductoDeleteView(DeleteView):
  model = Producto
  template_name = 'producto/producto_delete.html'
  success_url = reverse_lazy('producto:lista')

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['categorias'] = Categoria.objects.all()
    return context
