from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.forms import ModelForm
from .models import User


class UserCreationForm(ModelForm):
  password1 = forms.CharField(label='Password', widget=forms.PasswordInput())
  password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput())
  username = forms.CharField(widget=forms.TextInput)
  email = forms.CharField(widget=forms.TextInput())
  first_name = forms.CharField(widget=forms.TextInput)
  last_name = forms.CharField(widget=forms.TextInput)
  direction = forms.CharField(widget=forms.TextInput)
  country = forms.CharField(widget=forms.TextInput, required=False)
  telephone = forms.CharField(widget=forms.TextInput, required=False)
  avatar = forms.ImageField(widget=forms.FileInput, required=False)

  class Meta:
    model = User
    fields = (
      'username', 'email', 'password1', 'password2', 'first_name', 'last_name', 'direction',
      'country', 'telephone', 'avatar'
    )

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    for field in iter(self.fields):
      self.fields[field].widget.attrs.update({'class': 'form-control'})
    self.fields['email'].widget.attrs['autocomplete'] = 'nope'

  def clean_password2(self):
    password1 = self.cleaned_data.get('password1')
    password2 = self.cleaned_data.get('password2')

    if password1 and password2 and password1 != password2:
      raise forms.ValidationError('Passwords don\'t match')
    return password2

  def save(self, commit=True):
    user = super(UserCreationForm, self).save(commit=False)
    user.set_password(self.cleaned_data['password2'])
    if commit:
      user.save()
    return user


class UserChangeForm(ModelForm):
  password = ReadOnlyPasswordHashField()

  class Meta:
    model = User
    fields = '__all__'

  def clean_password(self):
    return self.initial['password']
