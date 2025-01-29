import socket
import dataMan

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
	
	variable_names = {"view_mode", "stamina", "speed", "head_angle", "kick", "dash", "turn", "say", "turn_neck", "catch", "move", "change_view"}
	
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
		print(f"sense_body = <{self.sense_body}>")
		print(f"view_mode = <{self.view_mode}>")
		print(f"stamina = <{self.stamina}>")
		print(f"speed = <{self.speed}>")
		print(f"head_angle = <{self.head_angle}>")
		print(f"kick = <{self.kick}>")
		print(f"dash = <{self.dash}>")
		print(f"turn = <{self.turn}>")
		print(f"say = <{self.say}>")
		print(f"turn_neck = <{self.turn_neck}>")
		print(f"catch = <{self.catch}>")
		print(f"move = <{self.move}>")
		print(f"change_view = <{self.change_view}>")
		print(f"serverTime: {self.serverTime}")
		
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
			self.view_mode = dataMan.strDiff("view_mode", s)
		elif "stamina" in s:
			self.stamina = dataMan.strDiff("stamina", s)
		elif "speed" in s:
			self.speed = dataMan.strDiff("speed", s)
		elif "head_angle" in s:
			self.head_angle = dataMan.strDiff("head_angle", s)
		elif "kick" in s:
			self.kick = dataMan.strDiff("kick", s)
		elif "dash" in s:
			self.dash = dataMan.strDiff("dash", s)
		elif "turn" in s:
			if "neck"in s:
				self.turn_neck = dataMan.strDiff("turn_neck", s)
			else:
				self.turn = dataMan.strDiff("turn", s)
		elif "say" in s:
			self.say = dataMan.strDiff("say", s)
		elif "catch" in s:
			self.catch = dataMan.strDiff("catch", s)
		elif "move" in s:
			self.move = dataMan.strDiff("move", s)
		elif "change_view" in s:
			self.change_view = dataMan.strDiff("change_view", s)
		else:
			print(f"in update_variable ERROR!!!\nno coincidence whith: ->{s}<-")
	
	def printVariableNames(self):
		print(self.variable_names)
		
	def serverTimeSync(self, response):
		
		if "see" in response:
			index = response.find("see") + len("see") + 1
		elif "sense_body" in response:
			index = response.find("sense_body") + len("sense_body") + 1
		else:
			print("ERROR!!! in syncing serer time")
			return -1
		
		s = ""
		while response[index] != " ":
			s += response[index]
			index += 1
			
		self.serverTime = s
		#print(f"s: <{s}>, serverTime: <{self.serverTime}>")
		
		return 0
		
	# REVCBE - CLASIFICA - ASIGNA, INFORMACION RECIBIDA DEL SERVIDOR
	# A SUS VARIABLES
	def updateState(self, response):
		# ESTA FUNCION SOLO ES PARA LOS COMANDOS RECIBIDOS YA FILTRADOS
		# OSEA SOLO PARA LO TIPO sense_body
		# init, server_param, player_type, sense_body, see
		# print(response)
		
		# TODO updateServerTime(string)
		
		for variable in self.variable_names:
			s = ""
			index = response.find(variable)
			
			while response[index] != ')':
				s += response[index]
				index += 1
			#print(f"in updateState() s: <{s}>")
			
			# ESTO FUNCIONARA DE MOMENTO PERO LO MAS SEGURO ES QUE
			# DADO QUE CONOCEMOS EL ORDEN EN EL QUE VIENEN LOS DATOS
			# EN EL COMANDO PODRIAMOS IR ACTUALIZANDO CADA UNA EN 
			# ESE ORDEN EN LUGAR DE TENER QUE BUSCAR CUAL ES LA QUE 
			# VAMOS A ACTUALIZAR EN CADA CICLO
			self.update_variable(s)
		return 0
	
	def getServerTime(self):
		return self.serverTime

	
