import socket

class Jugador:
	#ATRIBUTOS ASOCIADOS AL ESTADO DEL CUERPO DEL JUGADOR
	
	addres = "localhost"
	port = 6000
	socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	
	sense_body = "0"
	view_mode = "high normal"
	stamina = " 8000 1"
	speed = "0 0"
	head_angle = "0"
	kick = "0"
	dash = "0"
	turn = "0"
	say = "0"
	turn_neck = "0"
	catch = "0"
	move = "0"
	change_view = "0"
	
	#ATRUBUTOS ASOCIADOS AL SERVIDOR
	see = ""
	serverTime = "0"
	role = ""
	equip_name = "test"
	uniform_number = ""
	
	def __init__(self, role):
		self.role = role
	
	def sendCommand(self, message):
		self.socket.sendto(message.encode(), (self.addres, self.port))
		
	# ESTE METODO NO FUNCIONA	
	def getResponse(self):
		response, server = self.socket.recvfrom(1024)
		raw_response = r'{}'.format(response)
		return raw_response
		
	def printResponse(self):
		print(self.getResponse())
		
	def bye(self):
		self.sendCommand("(bye)")
		self.socket.close()
	
	# IMPRIME EN PANTALLA EL ESTADO DEL JUGADOR
	def printBodyState(self):
		print(f"sende_body = {self.sense_body}")
		print(f"view_mode = {self.view_mode}")
		print(f"stamina = {self.stamina}")
		print(f"speed = {self.speed}")
		print(f"head_angle{self.head_angle}")
		print(f"kick = {self.kick}")
		print(f"dash = {self.dash}")
		print(f"turn = {self.turn}")
		print(f"say = {self.say}")
		print(f"turn_neck = {self.turn_neck}")
		print(f"catch = {self.catch}")
		print(f"move = {self.move}")
		print(f"change_view = {self.change_view}")
		
	# REGRESA UNA STRING CON LOS VALORES DEL ESTADO DEL JUGADOR
	def getState(self):
		
		state = (self.sense_body + "\n" +
		self.view_mode + "\n" +
		self.stamina + "\n" +
		self.head_angle + "\n" +
		self.kick + "\n" +
		self.dash + "\n" +
		self.turn + "\n" +
		self.say + "\n" +
		self.turn_neck + "\n" +
		self.catch + "\n" +
		self.move + "\n" +
		self.change_view + "\n" +
		self.see + "\n" +
		self.serverTime + "\n" +
		self.role + "\n" +
		self.equip_name + "\n" +
		self.uniform_number + "\n")
		
		return state
		
		
	# RECIBE UNA CADENA Y ACTUALIZA LA VARIABLE A LA QUE ESTA HACIENDO
	# REFERENCIA DICHA CADENA
	def update_variable(self, s):
		if "view_mode" in s:
			index = s.find("view_mode") + 8
			sAux = ""
			while index <  len(s):
				sAux = sAux + s[index]
				index += 1
			self.view_mode = sAux
		
		elif "stamina" in s:
			index = s.find("stamina") + 7
			sAux = "" + s[index]
			index += 1
			while index < len(s):
				sAux = sAux + s[index]
				index += 1
			self.stamina = sAux
			
		elif "speed" in s:
			index = s.find("speed") + 5
			sAux = "" + s[index]
			index += 1
			while index < len(s):
				sAux = sAux + s[index]
				index += 1
			self.speed = sAux
			
		elif "head_angle" in s:
			index = s.find("head_angle") + 10
			sAux = "" + s[index]
			index += 1
			while index < len(s):
				sAux = sAux + s[index]
				index += 1
			self.head_angle = sAux
			
	
	# REVCBE - CLASIFICA - ASIGNA, INFORMACION RECIBIDA DEL SERVIDOR
	# A SUS VARIABLES
	def updateState(self):
		# DE MOMENTO IDENTIFICO 4 TIPOS DE COMANDOS QUE PUEDE RECIBIR
		# EL JUGADOR, init, server_param, player_type, sense_body, see
		response = self.getResponse()
		# print(response)
		variable_names = {"view_mode", "stamina", "speed", "head_angle"}
		
		index = 0
		if "sense_body" in response:
			
			# TODO updateServerTime(string)
			
			for variable in variable_names:
				
				s = ""
				index = response.find(variable)
				# print(f"in updateState(), for, variable: {variable}")
				# print(f"index: {index}")
				
				while response[index] != ')':
					s = s + response[index]
					index += 1
					
				# print(f"s: {s}")
				self.update_variable(s)
		
		return 0
	

	
