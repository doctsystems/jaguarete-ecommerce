from django.contrib import admin
from .models import Item, Order


class ItemInline(admin.TabularInline):
  model = Item
  raw_id_fields = ["producto"]
  extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
  list_display = ["__str__", "user_id", "nombre", "email", "is_pagado", "created", "modified"]
  list_filter = ["is_pagado", "created", "modified"]
  search_fields = ["nombre", "email", ]
  inlines = [
    ItemInline,
  ]
