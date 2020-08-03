class Account(object):
	"""Account Class"""

	def __init__(self, acNumber, fname, lname, balance):
		""" Account Constructor """

		self.acNumber = acNumber
		self._fname = fname
		self._lname = lname
		self.balance = balance
	

	def deposit(self, amount):

		self.balance += amount


	def withdraw(self, amount):

		self.balance -= amount

	
	def getBalance(self):

		return self.balance

	@property
	def getFirstName(self):

		return self._fname

	@property
	def getLastName(self):

		return self._lname



