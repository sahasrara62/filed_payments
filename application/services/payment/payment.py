import re
import datetime
from decimal import Decimal


def validate_card(card):
	if not re.search(r"^[456]\d{3}(-?\d{4}){3}$", card) or re.search(r"(\d)\1{3}", re.sub("-", "", card)):
		return False
	return True


class BaseCardDetails:
	def __init__(self):
		self.CreditCardNumber = None
		self.CardHolder = None
		self.ExpirationDate = None
		self.SecurityCode = None
		self.Amount = None


class Card(BaseCardDetails):
	def __init__(self):
		super(Card, self).__init__()
	
	def verify_input(self, **kwargs):
		"""
		CreditCardNumber(mandatory, string, it should be a valid credit card number)
		-CardHolder: (mandatory, string)
		-ExpirationDate (mandatory, DateTime, it cannot be in the past)
		-SecurityCode (optional, string, 3 digits)
		-Amount (mandatoy decimal, positive amount
		:param kwargs:
		:return:
		"""
		cards_value = ["CreditCardNumber", "CardHolder", "ExpirationDate", "Amount"]
		if set(cards_value).intersection(kwargs.keys()) != set(cards_value):
			print("card details not found")
			return False
		
		if not type(kwargs['CreditCardNumber'] == str and validate_card(kwargs['CreditCardNumber'])) or not len(kwargs['CreditCardNumber']) == 16:
			print("invalid credit card number")
			return False
		
		if not type(kwargs['CardHolder']) == str:
			print("card holder is not of string type")
			return False
		
		if kwargs.get('SecurityCode',None) :
			if not (type(kwargs.get('SecurityCode', None)) == str and len(kwargs.get('SecurityCode', None)) == 3) or not kwargs.get('SecurityCode', None).isdigit():
				print("security code error")
				return False

		if not datetime.datetime.strptime(kwargs['ExpirationDate'], "%Y/%m/%d") > datetime.datetime.now():
			print("date time error")
			return False
		
		try:
			if not Decimal(kwargs['Amount']) > 0:
				print("amount is invalid")
				return False
		except:
			return False
		
		_data_to_map = {
			"CreditCardNumber": kwargs['CreditCardNumber'],
			'Amount': kwargs['Amount'],
			'CardHolder': kwargs['CardHolder'],

			'ExpirationDate': kwargs['ExpirationDate']
		}
		if kwargs.get("SecurityCode", None):
			_data_to_map.update({"SecurityCode":kwargs.get("SecurityCode")})
		print("input is verified.")
		self.__map_to_card(**kwargs)
		return True
	
	def __map_to_card(self, **kwargs):
		self.CreditCardNumber = kwargs.get('CreditCardNumber', None)
		self.Amount = kwargs.get('Amount', None)
		self.CardHolder = kwargs.get('CardHolder', None)

		self.SecurityCode = kwargs.get('SecurityCode', None)
		self.ExpirationDate = kwargs.get('ExpirationDate', None)
		
		print("mapping of user input is done sucessfully.")
		return True
	
