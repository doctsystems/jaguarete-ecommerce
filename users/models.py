import os
from django.conf import settings
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils import timezone


class User(AbstractUser):

  direction = models.CharField(
    max_length=70,
    verbose_name='Direccion',
    null=True,
  )
  country = models.CharField(
    max_length=70,
    verbose_name='Pais',
    null=True,
  )
  telephone = models.CharField(
    max_length=70,
    verbose_name='Telefono',
    null=True,
  )
  avatar = models.ImageField(
    upload_to='img/users/',
    null=True
  )

  class Meta:
    verbose_name = 'Usuario'
    verbose_name_plural = 'Usuarios'
    ordering = ['-id']

  def __str__(self):
    return '{}, {}'.format(self.last_name, self.first_name)

  def get_avatar(self):
    if self.avatar:
      return self.avatar.url
    else:
      return os.path.join(settings.MEDIA_URL + str('img/nn.png'))


# class UserManager(BaseUserManager):

#   def create_user(self, email, username, password, **extra_fields):

#     if email is None:
#       raise TypeError('Ingrese una direccion de correo electrónico valida')
#     user=self.model(email=self.normalize_email(email), username=username, **extra_fields)
#     user.set_password(password)
#     user.save()
#     return user

#   def create_superuser(self, email, username, password, **extra_fields):

#     extra_fields.setdefault('is_staff', True)
#     extra_fields.setdefault('is_superuser', True)

#     if extra_fields.get('is_staff') is not True:
#       raise ValueError(_('El superusuario debe tener is_staff=True.'))
#     if extra_fields.get('is_superuser') is not True:
#       raise ValueError(_('El superusuario debe tener is_superuser=True.'))
#     return self.create_user(email, password, username, **extra_fields)
