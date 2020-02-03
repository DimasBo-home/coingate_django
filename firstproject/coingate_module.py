import requests

class Request:
	headers = None
	COINGATE_URL = "https://api-sandbox.coingate.com/v2/"
	response = None

	def __init__(self,headers):
		self.headers = headers

	def get(self,path,params=None):
		url = self.COINGATE_URL + path
		try:
			self.response = requests.get(url,params=params,headers=self.headers)
		except Exception as err:
			raise err

	def post(self,path,params=None):
		url = self.COINGATE_URL + path
		try:
			self.response = requests.post(url,params=params,headers=self.headers)
		except Exception as err:
				raise err

	def get_data(self):
		if self.response.ok and self.response.status_code == 200:
			return self.response.json()
		return None

class CoinGateClient(Request):

	def __init__(self, headers):
		super().__init__(headers)

	def request_test(self):
		"""
		Definition
		https://api-sandbox.coingate.com/v2/auth/test

		Result Format Content
		200 OK
		"""
		self.get("auth/test")
		
	def request_ping(self):
		"""
		Definition
		https://api-sandbox.coingate.com/v2/ping
		
		Result Format json
		200 OK
		{'ping': 'pong', 'time': '2020-02-01T17:58:28+00:00'}
		"""
		self.get("ping")
		
	def request_create_order(self,title,price_amount,price_currency,receive_currency,description=None):
		"""	
		Definition
		https://api.coingate.com/v2/orders

		Parameters
		"price_amount":1020.5,
		"price_currency":"EUR",
		"receive_currency":"BTC",
		"title":"test",
		"description":description,
		
		Result Format
		200 OK
		{
		  "id": 1195862,
		  "status": "new",
		  "price_currency": "USD",
		  "price_amount": "2000.0",
		  "receive_currency": "EUR",
		  "receive_amount": "",
		  "created_at": "2018-04-25T13:28:16+00:00",
		  "order_id": "111",
		  "payment_url": "https://coingate.com/invoice/6003de09-ee9a-4584-be0e-5c0c71c5e497",
		  "token": "MVsgsjGXv-pRWMnZzsuD4B5xcdnj-w"
		}
		"""
		params = {
			"order_id":"Tinatin-2020.31",
			"title":title,
			"price_amount":price_amount,
			"price_currency":price_currency,
			"receive_currency":receive_currency,
			"description":description,
		}

		print(title,price_amount,price_currency,receive_currency,description)
		self.post("orders",params)
		
	def request_get_list_order(self,per_page=100,page=1,sort="created_at_desc"):
		"""
		curl -H "Authorization: Token YOUR_APP_TOKEN" https://api.coingate.com/v2/orders/1195824
		"""
		params = {
			"per_page":per_page,
			"page":page,
			"sort":sort
		}

		self.get("orders",params)

	def request_get_order(self,order_id):
		"""
		Definition
		https://api.coingate.com/v2/orders/:id

		Parameters
		order_id int

		Result Format
		200 OK ·
		404 Not Found
		{
		  "id": 1195824,
		  "status": "paid",
		  "price_currency": "EUR",
		  "price_amount": "10.0",
		  "pay_currency": "BTC",
		  "pay_amount": "0.001281",
		  "receive_currency": "EUR",
		  "receive_amount": "9.9",
		  "created_at": "2018-04-24T23:43:14+00:00",
		  "expire_at": "2018-04-25T00:05:40+00:00",
		  "payment_address": "38gmr5MujyDxcEhaqFfC5P9K6bhJo548gu",
		  "order_id": "110",
		  "underpaid_amount": "0",
		  "overpaid_amount": "0",
		  "is_refundable": false,
		  "payment_url": "https://coingate.com/invoice/4f5e5a63-5270-435d-bf05-eec369b0fdba"
		}
		"""
		path = "orders/" + str(order_id)
		self.get(path)