from django.urls import path
from .views import Home, About, Buscar, Forbidden


urlpatterns = [
	path('', Home.as_view(), name='home'),
	path('about/', About.as_view(), name='about'),
	path('buscar/', Buscar, name='buscar'),
	path('403/', Forbidden.as_view(), name='forbidden'),
]