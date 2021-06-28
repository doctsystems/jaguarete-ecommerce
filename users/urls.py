from django.urls import path
from .views import Registro


urlpatterns = [
	path('register/', Registro, name='register'),
]