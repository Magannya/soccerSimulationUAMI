class Error_manager:
	
	def __init__(self):
		return 0
		
	def file_append(errorMessage):
		with open("debug_file", 'a') as file:
			file.write(errorMessage)
	
	def say_Hello(self):
		print("hello from Error_manager.");
