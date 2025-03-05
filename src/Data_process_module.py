import dataMan

class Data_process_module:
	
	playerAttrib = []
	debugModule = None
	
	def __init__(self):
		print("Comunication module init.")
		
	def sayHello(self):
		print("Hello from Data_process_module")
		
	# SETTERS Y GETTERS ------------------------------------------------
	
	# MAIN -------------------------------------------------------------
	
	def updateState(self, serverMessage):
		if "sense_body" in serverMessage:
			# TODO
			
		elif "see" in serverMessage:
			# TODO
			
		elif "hear" in serverMessage:
				
		else:
			
			
	# COMPLEMENTARY ----------------------------------------------------
