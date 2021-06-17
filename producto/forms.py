from django import forms
from .models import Producto


class ProductoForm(forms.ModelForm):

  def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['categoria'].widget.attrs['autofocus'] = True

	class Meta:
		model = Gasto
		fields = '__all__'
		exclude = ('is_pagado', 'cuotas_por_pagar', 'fecha',)
		widgets = {
			'categoria': forms.Select(attrs={
				'class': 'form-control select2', 'style': 'width: 100%;',
        'autocomplete': 'off'
				}),
			'descripcion': forms.Textarea(attrs={
				'placeholder': 'Ingrese descripcion del Gasto',
				'class': 'form-control',
        'autocomplete': 'off',
        'rows': 3,
        'cols': 3
				}),
			'monto': forms.TextInput(attrs={
				'placeholder': 'Ingrese el monto del Gasto',
				'class': 'form-control',
        'autocomplete': 'off'}),
			'nro_cuotas': forms.TextInput(attrs={
				'placeholder': 'Nro de cuotas en que se pagara el Gasto',
				'class': 'form-control',
        'autocomplete': 'off'}),
		}