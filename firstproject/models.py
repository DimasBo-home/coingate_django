from django.db import models
from django.shortcuts import reverse
from .coingate_django import create_order

class Order(models.Model):
	CURENNCY_CHOICES = [
		("EUR" ,"EUR"), 
		("USD" ,"USD"), 
		("CAD" ,"CAD"),
	]
	
	title = models.CharField(max_length=150)
	description = models.TextField(max_length=500,null=True,blank=True)
	request_id = models.PositiveIntegerField(null=True,blank=True)
	price_currency = models.CharField(max_length=3,choices=CURENNCY_CHOICES)
	price_amount = models.DecimalField(max_digits=9, decimal_places=2)
	receive_currency = models.CharField(max_length=3, default="BTC")

	def get_absolute_url(self):
		return reverse('order_detail_url', kwargs={"pk":self.pk})

	def __str__(self):
		return self.title

	def get_price_cutenncy(self):
		for choice in self.CURENNCY_CHOICES:
			if choice[0] == self.price_curenncy:
				return choice[1]
		return self.price_curenncy
	get_price_cutenncy.short_description = "Price Curenncy"
	
	def save(self,*args,**kwargs):
		data = create_order(self.title,self.price_amount,self.price_currency,self.receive_currency,self.description)
		print(data)
		self.request_id = data["id"]

		super().save(self,*args,**kwargs)

	class Meta:
		ordering = ["-id"]