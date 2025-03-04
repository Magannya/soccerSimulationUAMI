import socket
import dataMan

class Comunication_module:
	
	remaningResponse = None	
	addres = "Localhost"
	port = 6000
	socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	timeChange = True
	previousTime = 0
	
	def __init__(self):
		print("Comunication module init.")
	
	def sayHello(self):
		print("Hello from Comunication module.")
		
	# SETTERS Y GETTERS ------------------------------------------------
	
	def setRemaningResponse(self, response):
		self.remaningResponse = response	
	
	def getRemaningResponse(self):
		return self.remaningResponse
		
	
	# MAIN -------------------------------------------------------------
	def listenServer(self):
		response, server = self.socket.recvfrom(1024)
		response = response.decode('utf-8')
		self.timeChange = self.checkTimeChange(response)
		return response
		
		
	def respondServer(self, playerResponse):
		if self.timeChange:
			if self.remaningResponse is not None:
				self.socket.sendto(self.remaningResponse.encode(), (self.addres, self.port))
				self.remaningResponse = None
			else:
				self.socket.sendto(playerResponse.encode(), (self.addres, self.port))
		else:
			self.remaningResponse = playerResponse
			
	# COMPLEMENTARY ----------------------------------------------------
	
	def checkTimeChange(self, response):
		actualTime = dataMan.subStrToSpace(response, 1)
		if actualTime != self.previousTime:
			self.previousTime = actualTime
			return True
		else:
			return False
		
