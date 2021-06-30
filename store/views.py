from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from producto.models import Categoria, Producto


class Home(generic.TemplateView):
  template_name = 'store/home.html'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context["productos"] = Producto.objects.filter(is_disponible=True)[:10]
    return context


class About(generic.TemplateView):
  template_name = 'store/about.html'


@csrf_exempt
def Buscar(request):
  template_name = 'store/buscar.html'

  queryset = Producto.objects.filter(is_disponible=True)
  filter_slug = request.GET.get('f')
  if filter_slug:
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
      'page_obj': productos,
      'filtro': filter_slug
    }
    return render(request, template_name, context)
  else:
    return redirect('store:home')


class Forbidden(LoginRequiredMixin, generic.TemplateView):
  login_url = 'login'
  template_name = 'store/403.html'
