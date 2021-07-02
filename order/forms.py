from crispy_forms.helper import FormHelper
from crispy_forms.layout import Div, Field, Fieldset, Layout, Submit
from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):

  class Meta:
    model = Order
    fields = [
      "nombre",
      "email",
      "direccion",
      "numero",
      "descripcion",
      "ciudad",
    ]

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.helper = FormHelper()
    self.helper.form_method = "post"
    self.helper.form_action = "."
    self.helper.add_input(
      Submit(
        "submit",
        "Finalizar compra",
        css_class="btn btn-success btn-lg btn-block",
      )
    )
    self.helper.layout = Layout(
      Fieldset(
        "",
        "nombre",
        "email",
        Div(
          Field("ciudad", wrapper_class="col"),
          css_class="row",
        ),
        Div(
          Field("direccion", wrapper_class="col"),
          css_class="row",
        ),
        Div(
          Field("numero", wrapper_class="col"),
          Field("descripcion", wrapper_class="col"),
          css_class="row",
        ),
        css_class="border-bottom mb-3",
      )
    )
