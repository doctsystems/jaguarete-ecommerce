from django.contrib import admin
from django.contrib.auth import admin as auth_admin

from .forms import UserChangeForm, UserCreationForm
from .models import User


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
  form = UserChangeForm
  add_form = UserCreationForm

  list_display = (
    'id',
    'first_name',
    'last_name',
    'email',
    'is_staff',
    'is_active',
    'is_superuser',
  )
  list_filter = (
    'email',
    'is_staff',
    'is_active',
  )
  fieldsets = (
    ('User info', {
      'fields': ('email', 'password')
    }),
    (
      'Personal info', {
        'fields': (
          'first_name', 'last_name', 'direction', 'country', 'telephone',
          'avatar'
        )
      }
    ),
    ('Permissions', {
      'fields': ('is_active', 'is_staff')
    }),
  )
  add_fieldsets = (
    (None, {
      'classes': ('wide', ),
      'fields': ('email', 'password1', 'password2'),
    }),
  )
  search_fields = ('email', )
  ordering = ('-id', )
