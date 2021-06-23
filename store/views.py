from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from producto.models import Categoria, Producto


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


@csrf_exempt
def Buscar(request):
  template_name = 'store/buscar.html'

  if request.method == "POST":
    queryset = Producto.objects.filter(is_disponible=True)
    filter_slug = request.POST.get('f')
    query = queryset.filter(
      Q(nombre__icontains=filter_slug) | Q(descripcion__icontains=filter_slug)
    )
    page = request.GET.get('page', 1)
    paginator = Paginator(query, 3)
    try:
      productos = paginator.page(page)
    except PageNotAnInteger:
      productos = paginator.page(1)
    except EmptyPage:
      productos = paginator.page(paginator.num_pages)
    context = {
      'productos': productos,
      'categorias': Categoria.objects.all(),
      'filtro': filter_slug
    }
    return render(request, template_name, context)
