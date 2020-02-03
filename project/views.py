from django.shortcuts import render
from django.views.generic import CreateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Order
from .coingate_django import get_data_order, get_data_list_order
from django import forms

class OrderCreateView(CreateView):
	model = Order
	fields = ('price_currency','price_amount','receive_currency','title','description')
	template_name = 'order_create.html'
	
	def get_form(self):
		form = super().get_form()
		form.fields["receive_currency"].widget.attrs['readonly'] = True
		return form
  
class OrderDetailView(DetailView):
	model = Order
	template_name = "order_detail.html"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		order = get_data_order(context["order"].request_id)
		context["order"].status = order["status"]
		context["order"].receive_currency = order["receive_currency"]
		context["order"].receive_amount = 0 if order["receive_amount"] == '' else order["receive_amount"]
		context["order"].payment_url = order["payment_url"]
		context["order"].created_date = order["created_at"]
		return context

class ListOrderView(ListView):
	model = Order
	template_name = "index.html"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		list_order = get_data_list_order()
		for order in context["object_list"]:
			o = list(filter(lambda l: l["id"] == order.request_id, list_order["orders"]))[0]
			order.status = o["status"]
			order.created_date = o["created_at"]
		return context
