from Error_manager import Error_manager
from Print_manager import Print_manager


class Debug_module:
	
	errorManager = None
	printManager = None
	
	F_SERVER_FLAG = True
	F_PLAYER_FLAG = True
	
	def __init__(self):
		self.errorManager = Error_manager()
		self.printManager = Print_manager()
		print("debug init")
		
	def sayHello(self):
		print("Hello from Debug.")
		
	# MAIN--------------------------------------------------------------
	
	def errorMessage(self, message, mode):
		if mode == "s":
			self.printManager.sPrintAppend(message)
		elif mode == "d":
			self.printManager.dPrintAppend(message)
		elif mode == "f":
			self.errorManager.fileAppend(message)
		else:
			self.errorManager.fileAppend(message)
			self.printManager.dPrintAppend(message)
			
	def saveServerMessage(self, serverMessage):
		with open("serverMessages", "a", encoding="utf-8") as file:
			
			serverMessage.replace('\00', '')
			serverMessage += '\n'
				
			if self.F_SERVER_FLAG:
				file.truncate(0)
				self.F_SERVER_FLAG = False
				
			file.write(serverMessage)
			
	def savePlayerResponse(self, playerResponse):
		with open("playerResponses", "a", encoding="utf-8") as file:
			
			playerResponse.replace('\00', '')
			playerResponse += '\n'
				
			if self.F_SERVER_FLAG:
				file.truncate(0)
				self.F_SERVER_FLAG = False
				
			file.write(playerResponse)
			
	def screenRefresh(self):
		self.printManager.refresh()
