from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView
from cart.cart import Cart
from .forms import OrderCreateForm
from .models import Item, Order


class OrderCreateView(CreateView):
  model = Order
  form_class = OrderCreateForm

  def form_valid(self, form):
    cart = Cart(self.request)
    if cart:
      order = form.save(commit=False)
      order.user = self.request.user
      order.is_pagado = True
      order.save()
      for item in cart:
        Item.objects.create(
          orden=order,
          producto=item["producto"],
          precio=item["precio"],
          cantidad=item["cantidad"],
        )
      cart.clear()
      return render(self.request, 'order/order_created.html', {'order': order})
    return HttpResponseRedirect(reverse("store:home"))

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context["cart"] = Cart(self.request)
    return context
