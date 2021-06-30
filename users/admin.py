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
    'username',
    'email',
  )
  list_filter = (
    'username',
    'email',
  )
  fieldsets = (
    ('User info', {
      'fields': ('username', 'email', 'password')
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
    ('Groups', {
      'fields': ('groups',)
    }),
  )
  add_fieldsets = (
    (None, {
      'classes': ('wide', ),
      'fields': ('username', 'email', 'password1', 'password2'),
    }),
  )
  search_fields = ('username', 'email')
  ordering = ('-id', )
