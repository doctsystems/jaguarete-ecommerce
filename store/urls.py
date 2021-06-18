from django.urls import path
from .views import Home, About, Carrito


urlpatterns = [
	path('', Home.as_view(), name='home'),
	path('about/', About.as_view(), name='about'),
]