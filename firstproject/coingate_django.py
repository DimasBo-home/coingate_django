from .coingate_module import CoinGateClient
from django.conf import settings
from django.conf.urls.static import static

from firstproject.coingate_module import *
from django.conf import settings

def get_data_list_order(per_page=100):
	coin = CoinGateClient(settings.HEADERS)
	try:
		coin.request_get_list_order(per_page)
		data = coin.get_data()
		return data
	except:
		return "Error: no connection to the database or not connection network "+ str(coin.response)

def get_data_order(order_id):
	coin = CoinGateClient(settings.HEADERS)
	try:	
		coin.request_get_order(order_id)
		data = coin.get_data()
		return data
	except:
		return "Error: no connection to the database or not connection network "+ str(coin.response)
	
def create_order(title,price_amount,price_currency,receive_currency,description=None):
	coin = CoinGateClient(settings.HEADERS)
	try:
		coin.request_create_order(title,price_amount,price_currency,receive_currency,description)
		data = coin.get_data()
		return data
	except:
		return "Error: no connection to the database or not connection network "+ str(coin.response)