import Error_manager
import Print_manager

class Debug_module:
	
	errorManager = None
	printManager = None
	
	def __init__(self):
		self.errorManager = Error_manager()
		self.printManager = Print_manager()
		
	def say_Hello(self):
		print("Hello from Debug.")
