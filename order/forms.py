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
        "Realizar pedido",
        css_class="btn btn-success btn-lg btn-block",
      )
    )
    self.helper.layout = Layout(
      Fieldset(
        Div(
          Field("nombre", css_class="form-control", wrapper_class="col"),
          css_class="row",
        ),
        Div(
          Field("email", css_class="form-control", wrapper_class="col"),
          css_class="row",
        ),
        Div(
          Field("ciudad", css_class="form-control", wrapper_class="col"),
          css_class="row",
        ),
        Div(
          Field("direccion", css_class="form-control", wrapper_class="col"),
          css_class="row",
        ),
        Div(
          Field("numero", css_class="form-control", wrapper_class="col"),
          css_class="row",
        ),
        Div(
          Field("descripcion", css_class="form-control", wrapper_class="col"),
          css_class="row",
        ),
        css_class="border-bottom mb-3",
      )
    )
