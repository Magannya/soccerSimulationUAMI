class Error_manager:
	
	def __init__(self):
		print("Error_manager init.")
		
	def fileAppend(self, errorMessage):
		with open("debug_file", 'a') as file:
			errorMessage += '\n'
			file.truncate(0)
			file.write(errorMessage)
	
	def sayHello(self):
		print("hello from Error_manager.");
