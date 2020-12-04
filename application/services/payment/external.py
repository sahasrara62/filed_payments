from application.services.payment import Card


class BasePaymentGateway:
	def __init__(self, repeat=0):
		self.repeat = repeat
		self.gateway = None
		
	def __repr__(self):
		return "<{}>".format("BasePaymentGateway")
	
	def connect(self, gateway=None, details=None):
		if gateway != None:
			if self.authenticate(details):
				return True
		return False
	
	def authenticate(self, details=None):
		if details != None:
			return True
		return False
	
	def pay(self, amount, user_details=None, gateway=None):
		if gateway is None:
			gateway = self.gateway
		while self.repeat + 1 > 0:
			if self.connect(gateway, user_details):
				print("payment of {} in gateway {} sucessful".format(amount, self.gateway))
				return True
			self.repeat -= 1
		return False


class PremiumBasePaymentGateway(BasePaymentGateway):
	def __init__(self, repeat=3):
		super(PremiumBasePaymentGateway, self).__init__(repeat)
		self.gateway = "PremiumBasePaymentGatway"
	
	def __repr__(self):
		return "<PremiumBasePaymentGateway>"


class ExpensiveBasePaymentGateway(BasePaymentGateway):
	def __init__(self, repeat=1):
		super(ExpensiveBasePaymentGateway, self).__init__(repeat)
		self.gateway = "ExpensiveBasePaymentGateway"
	
	def __repr__(self):
		return "<ExpensiveBasePaymentGateway>"


class CheapBasePaymentGateway(BasePaymentGateway):
	def __init__(self, repeat=0):
		super(CheapBasePaymentGateway, self).__init__(repeat)
		self.gateway = "CheapBasePaymentGateway"
	
	def __repr__(self):
		return "<CheapBasePaymentGateway>"


class ExternalPayment:
	def __init__(self, amount, card_details=None):
		self.amount = amount
		self.card_details = card_details
	
	def make_payment(self):
		try:
			payment_mode = None
			if self.amount <= 20:
				payment_mode = CheapBasePaymentGateway()
			elif 20 < self.amount < 500:
				payment_mode = ExpensiveBasePaymentGateway()
			elif self.amount >= 500:
				payment_mode = PremiumBasePaymentGateway()
			else:
				return False
			
			status = payment_mode.pay(self.amount, self.card_details)
			return status
		except:
			return False

