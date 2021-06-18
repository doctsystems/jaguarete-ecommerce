from django import forms
from django.conf import settings

PRODUCTO_CANTIDAD_CHOICES = [
  (i, str(i)) for i in range(1, settings.CART_ITEM_MAX_CANTIDAD + 1)
]


class CartAddProductoForm(forms.Form):
  cantidad = forms.TypedChoiceField(
    label="Cantidad",
    choices=PRODUCTO_CANTIDAD_CHOICES,
    coerce=int
  )
  override = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
