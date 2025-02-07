import socket
import dataMan
import sys
import os


class Jugador:
	
	# ATRIBUTOS NESESARIOS PARA CONECTAR CON EL SERVIDOR
	addres = "localhost"
	port = 6000
	socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	
	# TAL VEZ DEBAMOS CAMBIAR ESTE TIPO POR 1, 2, 3 ETC SI QISIERAMOS
	# OPERAR CON ESTAS DOS VARIABLES
	view_mode1 = "high"
	view_mode2 = "normal"
	
	#ATRIBUTOS ASOCIADOS AL ESTADO DEL CUERPO DEL JUGADOR
	sense_body = "0"
	stamina = 0
	stamina_effort = 0
	speed = 0
	speed_angle = 0
	head_angle = 0
	kick = 0
	dash = 0
	turn = 0
	say = 0
	turn_neck = 0
	catch = 0
	move = 0
	change_view = 0
	
	see = ""
	
	# ESTA VARIABLE ES USADA PARA ACTUALIZAR LOS DATOS 
	variable_names = {"view_mode", "stamina", "speed", "head_angle", "kick", "dash", "turn", "say", "turn_neck", "catch", "move", "change_view"}
	
	#ATRUBUTOS ASOCIADOS AL SERVIDOR
	serverTime = 0
	previousServerTime = 0
	serverTimeChange = False
	role = ""
	equip_name = "test"
	uniform_number = ""
	
	# VARIABLES PARA GENERAR UN DICCIONARIO DE ERRORES 
	# O COSAS INUSUALES DURANTE LA EJECUCION
	errorSumary = "-"
	errorSumaryCount = 0
	
	# PARA FOCALIZARSE EN UN OBJETO DEL CAMPO Y PODER
	# TOMAR DESICIONES EN FUNCION DE LA INFORMACION QUE CONOCEMOS DE 
	# ESE OBJETO, NOMBRE, DISTANCIA Y ANGULO
	objectFocusName = ""
	objectFocusDirection = ""
	objectFocusAngle = ""
	
	def __init__(self, role):
		self.role = role
		self.sendCommand("(init eTest (version 7))")
		self.printResponse()
	
	def hello(self):
		print("hello from Jugador")
	
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
		print(f"view_mode = <{self.view_mode1}> | <{self.view_mode2}>")
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
		print(f"serverTime: <{self.serverTime}>")
		
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
		
	def printFocusObject(self):
		print("(" + self.objectFocusName + " " + self.objectFocusDirection + " " + self.objectFocusAngle + ")")
	
	def getServerTimeChange(self):
		return self.serverTimeChange
	
	def errorSumaryUpdate(self, error):
		self.errorSumary += self.errorSumary + "\n" + error
		
	def printErrorSumary(self):
		print(self.errorSumary)
	
	# RECIBE UNA CADENA Y ACTUALIZA LA VARIABLE A LA QUE ESTA HACIENDO
	# REFERENCIA DICHA CADENA
	def updateVariable(self, s):
		
		if "view_mode" in s:
			self.view_mode = dataMan.strDiff("view_mode", s)
		elif "stamina" in s:
			cad = dataMan.strDiff("stamina", s)
			cad1 = dataMan.subStrToSpace(cad, 0)
			cad2 = dataMan.subStrToSpace(cad, 1)
			
			self.stamina = float(cad1)
			self.stamina_effort = float(cad2)
			
		elif "speed" in s:
			cad = dataMan.strDiff("speed", s)
			cad1 = dataMan.subStrToSpace(cad, 0)
			cad2 = dataMan.subStrToSpace(cad, 1)
			
			self.speed = float(cad1)
			self.speed_angle = float(cad2)
			 
		elif "head_angle" in s:
			self.head_angle = float(dataMan.strDiff("head_angle", s))
			
		elif "kick" in s:
			self.kick = float(dataMan.strDiff("kick", s))
		elif "dash" in s:
			self.dash = float(dataMan.strDiff("dash", s))
		elif "turn" in s:
			if "neck"in s:
				self.turn_neck = float(dataMan.strDiff("turn_neck", s))
			else:
				self.turn = float(dataMan.strDiff("turn", s))
		elif "say" in s:
			self.say = float(dataMan.strDiff("say", s))
		elif "catch" in s:
			self.catch = float(dataMan.strDiff("catch", s))
		elif "move" in s:
			self.move = float(dataMan.strDiff("move", s))
		elif "change_view" in s:
			self.change_view = float(dataMan.strDiff("change_view", s))
		else:
			error = f"ERROR!!! in updateVariable(): no coincidence whith: <{s}>\n"
			self.errorSumaryUpdate(error)
			self.errorSumaryCount += 1
			print(error)
			return 1
		return 0
	
	# SOLO ERA PARA UNA PRUEBA, PODEMOS ELIMINARLA SI NO HACE FALTA
	def printVariableNames(self):
		print(self.variable_names)
		
	
	def serverTimeSync(self, response):
		
		if "see" in response:
			s = dataMan.subStrToNextWhite("see", response)
		elif "sense_body" in response:
			s = dataMan.subStrToNextWhite("sense_body", response)	
		elif "server_param" in response:
			s = dataMan.subStrToNextWhite("server_param", response)	
		elif "player_param" in response:
			s = dataMan.subStrToNextWhite("player_param", response)
		elif "hear" in response:
			s = dataMan.subStrToNextWhite("hear", response)
		elif "player_type" in response:
			s = dataMan.subStrToNextWhite("player_type", response)
		else:
			error = f"ERROR!!! in serverTimeSync(), response: <{response}>\n"
			self.errorSumaryUpdate(error)
			erorrSumaryCount += 1
			print(error)
			return 1
		
		
			
		#print(f"s: <{s}>, serverTime: <{self.serverTime}>")
		
		# SOLO SE ACTUALIZA SI HAY UNA DIFERENCIA ENTRE EL TIEMPO
		# REGISTRADO POR EL JUGADOR Y EL TIEMPO REPORTADO
		# POR EL SERVIDOR
		
		flotante = float(s)
		if flotante != self.previousServerTime:
			self.previousServerTime = self.serverTime
			self.serverTime = flotante
			self.serverTimeChange = True
			return 0
		else:
			self.serverTimeChange = False
			return -1
		
		
	# REVCBE - CLASIFICA - ASIGNA, INFORMACION RECIBIDA DEL SERVIDOR
	# A SUS VARIABLES
	def updateState(self):
		# ESTA FUNCION SOLO ES PARA LOS COMANDOS RECIBIDOS YA FILTRADOS
		# OSEA SOLO PARA LO TIPO sense_body.
		
		# init, server_param, player_type, sense_body, see
		
		# SE RECIBEN MUCHOS COMANDO DEL SERVIDOR DEL TIPO
		# server_param Y player_type
		
		# SYNCRONIZACION DEL TIEMPO DEL SERVIDOR CON EL TIEMPO 
		# REGISTRADO POR EL JUGADOR
		response = self.getResponse()
		self.serverTimeSync(response)
		
		if "sense_body" in response:
			
			for variable in self.variable_names:
				s = ""
				index = response.find(variable)
			
				while response[index] != ')':
					s += response[index]
					index += 1
				self.updateVariable(s)
			
			# ESTO FUNCIONARA DE MOMENTO PERO LO MAS SEGURO ES QUE
			# DADO QUE CONOCEMOS EL ORDEN EN EL QUE VIENEN LOS DATOS
			# EN EL COMANDO PODRIAMOS IR ACTUALIZANDO CADA UNA EN 
			# ESE ORDEN EN LUGAR DE TENER QUE BUSCAR CUAL ES LA QUE 
			# VAMOS A ACTUALIZAR EN CADA CICLO
			
			
		elif "see" in response:
			self.see = response
			
		else:
			error = f"ERROR !!! in updateState() unknown response: <{response}>"
			self.errorSumaryUpdate(error)
			self.errorSumaryCount += 1
			print(error)
			
			return 1
			
		return 0
	
	def getServerTime(self):
		return self.serverTime
		
	def setSee(self, response):
		self.see = response
		
	# LE DAS EL NOMBRE DE UN OBJETO EN EL CAMP0 Y TE REGRESA LA
	# INFORMACION DE SU DISTANCIA Y SU ANGULO
	def getObjectInfo(self, objectName):
		
		if objectName in self.see:
			
			objectInfo = ""
			
			index = self.see.find(objectName) + len(objectName) + 1
			
			while self.see[index] != ')':
				objectInfo += self.see[index]
				index += 1
			
			return objectInfo
		else:
			error = "in setObjectFocus() object not in see response"
			self.errorSumaryUpdate(error)
			print(error)
			self.errorSumaryCount += 1
			return None
		
	# SETEA LA INFORMACION DEL OBJETO EN CUESTION	
	def setObjectFocus(self, objectName):
		objectInfo = self.getObjectInfo(objectName)
		#print(objectInfo)
		if objectInfo != None:
			self.objectFocusName = objectName
			objectDirection = ""
			objectAngle = ""
			b = False
			
			for c in objectInfo:
				if c == " ":
					b = True
					continue
					
				if b:
					objectAngle += c
				else:
					objectDirection += c
			
			self.objectFocusDirection = objectDirection
			self.objectFocusAngle = objectAngle
			
			return True
		else:
			return False
			
	def getFocusObjectDirection(self):
		return self.objectFocusDirection
		
	def getFocusObjectAngle(self):
		return self.objectFocusAngle
		
	# CHECAR ESTO POR QUE NO ME CUADRA BIEN LA FORMA DE CASTEAR
	# TODOS LOS DATOS DEL AGENTE PARA OPERAR CON ELLOS
	
	# ESTO FUNCIONA PERO LO QUE NO ME CONVENCE ES EL DINAMISMO DE LOS
	# DATOS, PROBABLEMENTE ESTEMOS PERDIENDO INFORMACION POR LA RIGIDEZ
	# DE ESTOS METODOS, ESOTY PENSANDO EN HACER ALGUN METODO PARA LA 
	# VALIDACION DE LOS DATOS Y CORROBORAR QUE HAY LA CANTIDAD DE DATOS
	# QUE ESTAMOS PROCESANDO, EN CASO CONTRARIO HACER UN REPORTE 
	# PARA SABER SOBRE LOS  NUEVOS DATOS QUE NO ESTAMOS CONTEMPLANDO, 
	# INVESTIGAR SOBRE ESTOS Y PODER TENER UN MEJOR CONTROL.
	def getStamina(self):
		out = dataMan.subStrToFirtsSpace(self.stamina)
		return float(out)
	
