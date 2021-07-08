from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import AnonymousUser
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from cart.forms import CartAddProductoForm
from .models import Categoria, Producto
from .forms import ProductoForm


class ProductoListView(ListView):
  categoria = None
  paginate_by = 6
  extra_context = {"form": CartAddProductoForm()}

  def get_queryset(self):
    queryset = Producto.objects.filter(is_disponible=True)

    categoria_slug = self.kwargs.get("slug")
    if categoria_slug:
      self.categoria = get_object_or_404(Categoria, slug=categoria_slug)
      queryset = queryset.filter(categoria=self.categoria)

    filter_slug = self.kwargs.get("filter")
    if filter_slug:
      queryset = queryset.filter(
        Q(nombre__icontains=filter_slug) | Q(descripcion__icontains=filter_slug)
      )
    return queryset

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context["categoria"] = self.categoria
    context["filter"] = self.kwargs.get("filter")
    return context


class ProductoDetailView(DetailView):
  queryset = Producto.objects.filter(is_disponible=True)
  extra_context = {"form": CartAddProductoForm()}

  def handle_no_permission(self):
    if not self.request.user == AnonymousUser():
      self.login_url = 'store:forbidden'
    return HttpResponseRedirect(reverse_lazy(self.login_url))


class ProductoCreateView(PermissionRequiredMixin, CreateView):
  model = Producto
  template_name = 'producto/producto_create.html'
  form_class = ProductoForm
  success_url = reverse_lazy('producto:lista')
  permission_required = 'producto.add_producto'
  login_url = 'login'

  def post(self, request, *args, **kwargs):
    form = ProductoForm(request.POST, request.FILES)
    if form.is_valid():
      form.save()
      return HttpResponseRedirect(self.success_url)
    self.object = None
    context = self.get_context_data(**kwargs)
    # context['categorias'] = Categoria.objects.all()
    context['form'] = form
    return render(request, self.template_name, context)

  def handle_no_permission(self):
    if not self.request.user == AnonymousUser():
      self.login_url = 'store:forbidden'
    return HttpResponseRedirect(reverse_lazy(self.login_url))


class ProductoUpdateView(PermissionRequiredMixin, UpdateView):
  model = Producto
  form_class = ProductoForm
  template_name = 'producto/producto_update.html'
  success_url = reverse_lazy('producto:lista')
  permission_required = 'producto.change_producto'
  login_url = 'login'

  def handle_no_permission(self):
    if not self.request.user == AnonymousUser():
      self.login_url = 'store:forbidden'
    return HttpResponseRedirect(reverse_lazy(self.login_url))


class ProductoDeleteView(PermissionRequiredMixin, DeleteView):
  model = Producto
  template_name = 'producto/producto_delete.html'
  success_url = reverse_lazy('producto:lista')
  permission_required = 'producto.delete_producto'
  login_url = 'login'

  def handle_no_permission(self):
    if not self.request.user == AnonymousUser():
      self.login_url = 'store:forbidden'
    return HttpResponseRedirect(reverse_lazy(self.login_url))
