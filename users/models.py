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
    blank=True
  )
  country = models.CharField(
    max_length=70,
    verbose_name='Pais',
    null=True,
    blank=True
  )
  telephone = models.CharField(
    max_length=70,
    verbose_name='Telefono',
    null=True,
    blank=True
  )
  avatar = models.ImageField(
    upload_to='img/users/',
    null=True,
    blank=True
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
