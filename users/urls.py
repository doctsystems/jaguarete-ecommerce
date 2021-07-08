from django.urls import path
from .views import Registro, Dashboard


urlpatterns = [
	path('register/', Registro, name='register'),
	path('dashboard/', Dashboard.as_view(), name='dashboard'),
]