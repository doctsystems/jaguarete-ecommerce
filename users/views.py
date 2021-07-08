from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import generic
from .forms import *
from order.models import Order

User = get_user_model()

class Dashboard(LoginRequiredMixin, generic.TemplateView):
  template_name = 'users/dashboard.html'
  extra_context = {"form": UserChangeForm()}
  login_url = 'login'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['ordenes'] = Order.objects.filter(user=self.request.user)
    return context


def Registro(request):

  if request.user.is_authenticated:
    return redirect('store:home')

  if request.method == 'POST':
    registerForm = UserCreationForm(request.POST, request.FILES)
    if registerForm.is_valid():
      user = registerForm.save(commit=False)
      user.set_password(registerForm.cleaned_data['password1'])
      user.is_active = True
      user.save()
      # my_group = Group.objects.get(name=request.POST.get('accountGroup'))
      my_group = Group.objects.get(name='usuario')
      my_group.user_set.add(user)
      # current_site = get_current_site(request)
      # subject = 'Activate your Account'
      # message = render_to_string('account/registration/account_activation_email.html', {
      #     'user': user,
      #     'domain': current_site.domain,
      #     'uid': urlsafe_base64_encode(force_bytes(user.pk)),
      #     'token': account_activation_token.make_token(user),
      # })
      # user.email_user(subject=subject, message=message)
      return HttpResponseRedirect(reverse('login'))
  else:
    registerForm = UserCreationForm()
  return render(request, 'registration/registro.html', {'form': registerForm})