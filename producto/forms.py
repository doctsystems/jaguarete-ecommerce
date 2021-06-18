from django import forms
from .models import Producto


class ProductoForm(forms.ModelForm):

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.fields['categoria'].widget.attrs['autofocus'] = True

  class Meta:
    model = Producto
    fields = ('categoria', 'descripcion', 'nombre', 'precio', 'imagen')
    widgets = {
      'categoria':
      forms.Select(
        attrs={
          'class': 'form-control select2',
          'style': 'width: 100%;',
          'autocomplete': 'off'
        }
      ),
      'nombre':
      forms.TextInput(
        attrs={
          'placeholder': 'Ingrese el nombre del Producto',
          'class': 'form-control',
          'autocomplete': 'off'
        }
      ),
      'descripcion':
      forms.Textarea(
        attrs={
          'placeholder': 'Ingrese descripcion del Producto',
          'class': 'form-control',
          'autocomplete': 'off',
          'rows': 5,
          'cols': 5
        }
      ),
      'precio':
      forms.TextInput(
        attrs={
          'placeholder': 'Precio del Producto',
          'class': 'form-control',
          'autocomplete': 'off'
        }
      ),
    }

  imagen = forms.ImageField(
    widget=forms.FileInput(attrs={
      'class': 'form-control',
      'autocomplete': 'off'
    }),
    label='Imagen del producto'
  )
