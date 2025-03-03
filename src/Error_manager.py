class Error_manager:
	
	F_FLAG = True
	
	def __init__(self):
		print("Error_manager init.")
		
	def fileAppend(self, errorMessage):
		with open("debug_file", 'a') as file:
			errorMessage += '\n'
			
			if self.F_FLAG:
				file.truncate(0)
				self.F_FLAG = False
				
			file.write(errorMessage)
	
	def sayHello(self):
		print("hello from Error_manager.");
