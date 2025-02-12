import socket
import dataMan
import sys
import os
import time


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
	hear = ""
	
	# ESTA VARIABLE ES USADA PARA ACTUALIZAR LOS DATOS 
	variable_names = {"view_mode", "stamina", "speed", "head_angle", "kick", "dash", "turn", "say", "turn_neck", "catch", "move", "change_view"}
	
	#ATRUBUTOS ASOCIADOS AL SERVIDOR
	serverTime = 0
	gamePhase = ""
	lastCommand = ""
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
	objectFocusDirection = 0
	objectFocusAngle = 0	
	
	# VARIABLE PARA IMPRIMIR EN PANTALLA
	printQueue = ""
	refreshInterval = 0.1
	lastRefreshTime = 0
	finalReport = ""
	
	def __init__(self, role):
		self.role = role
		#self.sendCommand("(init eTest (version 7))")
		#self.printResponse()
	
	def setTurn(self, value):
		self.turn = value
		
	def getTurn(self):
		return self.turn
	
	def sendCommand(self, message):
		self.socket.sendto(message.encode(), (self.addres, self.port))
		
	# MANDA UN COMANDO AL SERVIDOR SOLO CUANDO HAY UN NUEVO CICLO EN 
	# EL SERVIDOR, ESTO PARA EVITAR SATURAR EL SERVIDOR CON EL 
	# MISMO COMANDO Y TRATAR DE GARANTIZAR LA EJECUCION DE EL COMANDO
	# QUE SE ESTA TRATANDO DE MANDAR	
	def sendResponse(self, response):
		if self.serverTimeChange:
			self.sendCommand(response)
			#print(f"response sended succesfully: {response}, {self.serverTime}")
			self.lastCommand = response
		
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
		print(f"gamePhase: <{self.gamePhase}>")
		print(f"objectFocus: ((<{self.objectFocusName}>) {self.objectFocusDirection} {self.objectFocusAngle})")
		print(f"lastCommand: <{self.lastCommand}>")
		
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
		
	def setSee(self, s):
		self.see = s
		
	def getSee(self):
		return self.see
		
	def printFocusObject(self):
		print("(" + self.objectFocusName + " " + self.objectFocusDirection + " " + self.objectFocusAngle + ")")
	
	def getServerTimeChange(self):
		return self.serverTimeChange
	
	# TENGO LA SOSPECHA DE QUE ESTE METODO ESTA HAICENDO QUE EL 
	# SCRIPT LLENE LA MEMORIA
	def errorSumaryUpdate(self, error):
		#self.errorSumary += self.errorSumary + "\n" + error
		#print("-")
		return 0
		
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
	
	def serverTimeSync(self, response):
		
		if "init" in response:
			return 0
		elif "server_param" in response:
			return 0
		elif "player_param" in response:
			return 0
		elif "player_type" in response:
			return 0
		elif "moving_to" in response:
			return 0
			
		auxST = dataMan.subStrToSpace(response, 1)
		# SOLO SE ACTUALIZA SI HAY UNA DIFERENCIA ENTRE EL TIEMPO
		# REGISTRADO POR EL JUGADOR Y EL TIEMPO REPORTADO
		# POR EL SERVIDOR
		
		flotante = 0
		
		try:
			flotante = float(auxST)
			
		except Exception as e:
			print(f"ERROR!!! in serverTimeSync() failed to convert <{flotante}> to float.")
			return 1
		
		if flotante != self.previousServerTime:
			self.previousServerTime = self.serverTime
			self.serverTime = flotante
			self.serverTimeChange = True
			return 0
		else:
			self.serverTimeChange = False
			return -1
		
	def gamePhaseUpdate(self, response):
		
		index = response.find("referee") + 8
		out = ""
		
		while response[index] != ')':
			out += response[index]
			index += 1
			
		self.gamePhase = out
		
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
		
		# OJO POR QUE HAY COMANDOS QUE NO CONTIENEN TIEMPO DEL SERVIDOR
		# MAS BIEN DEBERIAMOS EMPEZAR A SINCRONIZAR EL TIEMPO 
		# CUANDO EL PARTIDO HAYA EMPEZADO
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
			self.setSee(response)
		
		elif "hear" in response:
			self.hear = response
			
			if "referee" in response:
				self.gamePhaseUpdate(response)
				
		else:
			error = f"ERROR !!! in updateState() unknown response: <{response}>"
			self.errorSumaryUpdate(error)
			self.errorSumaryCount += 1
			print(error)
			
			return 1
			
		return 0
	
	def getServerTime(self):
		return self.serverTime
			
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
			#print(error)
			self.errorSumaryCount += 1
			return None
	
	def getObjectAttrib(self, objectName, c):
		if objectName in self.see:
			objectInfo = self.getObjectInfo(objectName)
			if c == 'd':
				distance = dataMan.subStrToSpace(objectName, 0)
				return distance
			elif c == 'a':
				angle = dataMan.subStrToSpace(objectName, 1)
				return angle
			else:
				error = "Error in getObjectAttrib(), invalid indentifier."
				print(error)
		else:
			return None
		
	# SETEA LA INFORMACION DEL OBJETO EN CUESTION	
	def setFocusObject(self, objectName):
		objectInfo = self.getObjectInfo(objectName)
		#print(objectInfo)
		
		if objectInfo != None:
			
			#print(f"objectInfo:<{objectInfo}>")
			self.objectFocusName = objectName
			objectDirection = dataMan.subStrToSpace(objectInfo, 0)
			objectAngle = dataMan.subStrToSpace(objectInfo, 1)
			
			# USANDO ESTE METODO ESTAMOS PERDIENDO INFORMACION
			# POR QUE ESTA ECHO PARA PROCESAR COMANDOS COMO EL SIGUIENTE
			# -x -x -x -x
			# NO HE INVESTIGADO QUE SIGNIFICAN LOS SIGUIENTES DATOS
			
			try:
				self.objectFocusDirection = float(objectDirection)
			except Exception as e:
				print(f"failed to convert objectDirection: {objectDirection}.")
				
			try:	
				self.objectFocusAngle = float(objectAngle)
			except Exception as e:
				print(f"failed to convert objectAngle: {objectAngle}.")
			
			return True
		else:
			# VOY A RESETEAR LA INFORMACION DEL OBJETO EN EL QUE SE 
			# ESTA ENFOCANDO PERO SOLO POR CUESTIONES DE IMPRESION EN 
			# PANTALLA, NO HACE FALTA HACERLO HAY QUE BORRARLO AL FINAL
			
			self.objectFocusName = None
			self.objectFocusDirection = None
			self.objectFocusAngle = None
			return False
			
	def getFocusObjectDirection(self):
		return self.objectFocusDirection
		
	def getFocusObjectAngle(self):
		return self.objectFocusAngle
		
		
	def getFocusObjectAll(self):
		return f"(<{self.objectFocusName}> <{self.objectFocusDirection}> <{self.objectFocusAngle}>)"
	# CHECAR ESTO POR QUE NO ME CUADRA BIEN LA FORMA DE CASTEAR
	# TODOS LOS DATOS DEL AGENTE PARA OPERAR CON ELLOS
	
	# ESTO FUNCIONA PERO LO QUE NO ME CONVENCE ES EL DINAMISMO DE LOS
	# DATOS, PROBABLEMENTE ESTEMOS PERDIENDO INFORMACION POR LA RIGIDEZ
	# DE ESTOS METODOS, ESOTY PENSANDO EN HACER ALGUN METODO PARA LA 
	# VALIDACION DE LOS DATOS Y CORROBORAR QUE HAY LA CANTIDAD DE DATOS
	# QUE ESTAMOS PROCESANDO, EN CASO CONTRARIO HACER UN REPORTE 
	# PARA SABER SOBRE LOS  NUEVOS DATOS QUE NO ESTAMOS CONTEMPLANDO, 
	# INVESTIGAR SOBRE ESTOS Y PODER TENER UN MEJOR CONTROL.


	# LAS SIGUIENTES FUNCIONES SERVIRAN PARA GESTIONAR LA IMPRESION
	# DE INFORMACION EN PANTALLA Y NO SATURAR DEMAS LA CONSOLA
	# -> TAL VEZ PODAMOS DIVIDIR ESTAS VARIABLES EN UNA ESTATICA Y 
	# UNA DINAMICA, ASI OPDRIAOMS TENER INFORMACION POR ALGUNOS CICLOS
	# Y QUITARLA CUANDO YA NO SEA NESESARIA
	def printAppend(self, s):
		self.printQueue += s
		self.printQueue += "\n"
	
	def refresh(self):
		if time.time() > self.lastRefreshTime + self.refreshInterval:
			os.system('clear')
			self.printBodyState()
			print("printQueue: " + self.printQueue)
			
			# RESETEO
			self.printQueue = ""
			self.lastRefreshTime = time.time()
			return 0
		else:
			return 1
				
	def refreshForce(self):
		os.system('clear')
		self.printBodyState()
		print(self.printQueue)
	
	def finalReportAppend(self, s):
		self.finalReport += f"{s}\n"
		
	def printFinalReport(self):
		print("Final report:")
		print(self.finalReport)
		
	
