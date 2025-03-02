from Error_manager import Error_manager
from Print_manager import Print_manager


class Debug_module:
	
	errorManager = None
	printManager = None
	
	def __init__(self):
		self.errorManager = Error_manager()
		self.printManager = Print_manager()
		print("debug init")
		
	def sayHello(self):
		print("Hello from Debug.")
