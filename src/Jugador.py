import socket
import dataMan
import sys
import os
import time
import random

from basic_math import *
from basic_movement import *

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
	stamina = 0
	stamina_effort = 0
	speed = 0
	speed_angle = 0
	head_angle = 0
	kick = 0	
	dash = 0
	turn = 0
	say = ""
	turn_neck = 0
	catch = 0
	move = 0
	change_view = ""
	
	see = ""
	hear = ""
	
	neckPosition = "0"

	# ESTA VARIABLE ES USADA PARA ACTUALIZAR LOS DATOS 
	variable_names = {"view_mode", "stamina", "speed", "head_angle", "kick", "dash", "turn", "say", "turn_neck", "catch", "move", "change_view"}
	
	#ATRUBUTOS ASOCIADOS AL SERVIDOR
	serverTime = 0
	gamePhase = ""
	previousServerTime = 0
	serverTimeChange = False
	role = ""
	teamName = ""
	teamSide = ""
	enemySide = ""
	uniformNumber = ""
	teamName = ""
	
	serverMessage = ""


	# VARIABLES PARA GENERAR UN DICCIONARIO DE ERRORES 
	# O COSAS INUSUALES DURANTE LA EJECUCION
	errorSumary = "-"
	errorSumaryCount = 0
	
	# PARA FOCALIZARSE EN UN OBJETO DEL CAMPO Y PODER
	# TOMAR DESICIONES EN FUNCION DE LA INFORMACION QUE CONOCEMOS DE 
	# ESE OBJETO, NOMBRE, DISTANCIA Y ANGULO
	focusObjectName = ""
	focusObjectDistance = 0
	focusObjectAngle = 0
	
	# VARIABLE PARA IMPRIMIR EN PANTALLA
	printQueue = ""
	refreshInterval = 0.1
	lastRefreshTime = 0
	finalReport = ""
	
	# CONTROL DE FLUJO
	fluxphase = ""
	lastCommand = ""
	commandQueue = None
	
	def __init__(self, role, teamName):
		self.role = role
		self.teamName = teamName
		self.sendCommand(f"(init {self.teamName} (version 14))")
		self.printResponse()
		
		#DE MOMENTO VAMOSA INICIALIZARLOS EN UNA POSICION ALEATORIA
		x = random.randint(-20, 20)
		y = random.randint(-20, 20)
		self.sendCommand(f"move({x} {y})")
		
	# SETERS Y GETERS
	
	# BODY--------------------------------------------------------------
	def setSpeedAngle(self, speed_angle):
		self.speed_angle = speed_angle
		
	def getSpeedAngle(self):
		return self.speed_angle
	
	def setTurn(self, value):
		self.turn = value
		
	def getTurn(self):
		return self.turn
		
	def setSee(self, s):
		self.see = s
		
	def getSee(self):
		return self.see
		
	# FOCUS OBJECTS-----------------------------------------------------
	def getfoDistance(self):
		return self.focusObjectDistance
		
	def getfoAngle(self):
		return self.focusObjectAngle
		
	# PLAYER RELATED----------------------------------------------------
	def setTeamName(self, teamName):
		self.teamName = teamName
	
	def getTeamName(self):
		return self.teamName
		
	def setTeamSide(self, teamSide):
		self.teamSide = teamSide
		
	def getTeamSide(self):
		return self.teamSide
		
	def setUniformNumber(self, uniformNumber):
		self.uniformNumber = uniformNumber
		
	def getUniformNumber(self):
		return self.uniformNumber
		
	def setEnemySide(self, enemySide):
		self.enemySide = enemySide
		
	def getEnemySide(self):
		return self.enemySide
	
	def printFocusObject(self):
		print("(" + self.focusObjectName + " " + self.focusObjectDistance + " " + self.focusObjectAngle + ")")
	
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
		
	# SERVER RELATED----------------------------------------------------
	def setServerTime(self, serverTime):
		self.serverTime = serverTime
		
	def getServerTime(self):
		return self.serverTime
		
	def setGamePhase(self, gamePhase):
		self.gamePhase = gamePhase
		
	def getGamePhase(self):
		return self.gamePhase
	
	# FLUX CONTROL------------------------------------------------------
	def setFluxPhase(self, phase):
		self.fluxphase = phase
		
	def getFluxPhase(self):
		return self.fluxphase
		
	def setLastCommand(self, message):
		self.lastCommand = message
	
	def getLastCommand(self):
		return self.lastCommand
		
	def setCommandQueue(self, message):
		self.commandQueue = message
		
	def getCommandQuere(self):
		return self.commandQueue
	
	#--------------INICIO BUCLE PRINCIPAL-------------------------------
	
	# INICIA EL BUCLE DEL JUGADOR EN EL QUE SE GESTIONAN TODOS SUS
	# PROCESOS PARA DETERMINAR SUS ACCIONES
	def start(self):
		gameOver = False
		message = ""
		
		while not gameOver:
			
			self.refresh()
			
			if self.commandQueue == None:
				self.updateState()
				message = self.think()
				self.sendResponse(message)
				
			else:
				sendResponse(self.commandQueue)
			
			gameOver = updateGameState()
			
		self.bye()
	
	# LA FUNCION MAS IMPORTANTE AQUI SE HARAN TOOS LOS CALCULOS 
	# PARA CONSTRUIR EL COMANDO QUE SE VA A RESPONER AL SERVIDOR
	# ESTO DEPENDERA DEL ROL DEL JUGADOR ASI COMO DE EL OBJETIVO
	# INDIVIDUAL EN TIEMPO REAL
	def think(self):
		message = ""
		
		#DEPENDIENDO DEL ESTADO DEL JUGADOR RESPONDEMOS
		if "before_kickoff" in self.gamePhase:
			
			# BUSCA LA PELOTA
			search_object("(b)")
			
		elif "play_on" in self.gamePhase:
			
			intercept_object("(b)")
		else:
			# TODO
			return 0
			#DEBUG ERROR, gamePhase NO RECONOCIDA
			
		message = self.buildCommand()
		return message
	
	# ESTA FUNCION MANEJARA TODAS LAS POSIBLES CONDICIONES DE 
	# PARADA PARA QUE EL JUGADOR MANDE SU COMANDO PARA DESCONECTARSE
	# DEL SERVIDOR
	def updateGamestate(self):
		# TODO
		gameOver = False
		
		return gameOver
	
	# DESPUES DE HACER LOS CALCULOS PERTINENTES PARA DETERMINAR CUAL
	# ES EL NUEVO OBJETIVO INDIVIDUAL SE CONSTRUYE EL COMANDO PARA 
	# MOVERSE A ESE OBJETIVO
	def buildCommand(self, message):
		
		self.serverMessage += message
	
	#--------------------FIN BUCLE PRINCIPAL----------------------------
	
	# -----METODOS RELACIONADOS A LA COMUNICACION CON EL SERVIDOR-------
	def sendCommand(self, message):
		self.socket.sendto(message.encode(), (self.addres, self.port))
		self.lastCommand = message
		
	# MANDA UN COMANDO AL SERVIDOR SOLO CUANDO HAY UN NUEVO CICLO EN 
	# EL SERVIDOR, ESTO PARA EVITAR SATURAR EL SERVIDOR CON EL 
	# MISMO COMANDO Y TRATAR DE GARANTIZAR LA EJECUCION DE EL COMANDO
	# QUE SE ESTA TRATANDO DE MANDAR	
	def sendResponse(self):
		
		if self.serverTimeChange:
			self.sendCommand(self.serverMessage)
			self.lastCommand = self.serverMessage
			self.serverMessage = ""
			self.commandQueue = None
		else:
			self.commandQueue = self.serverMessage
		
	def getResponse(self):
		response, server = self.socket.recvfrom(1024)
		raw_response = r'{}'.format(response)
		return raw_response
		
	def printResponse(self):
		print(self.getResponse())
		
	def bye(self):
		self.sendCommand("(bye)")
		self.socket.close()
	
	#--------------------METODOS DEBUG----------------------------------
	def printBodyState(self):
		print(f"teamName = <{self.teamName}>")
		print(f"teamSide = <{self.teamSide}>")
		print(f"uniformNumber = <{self.uniformNumber}>")
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
		print(f"hear: <{self.hear}>")
		print(f"focusObject: ({self.focusObjectName} {self.focusObjectDistance} {self.focusObjectAngle})")
		print(f"lastCommand: <{self.lastCommand}>")
		
	
	def getFocusObjectAll(self):
		return f"(<{self.focusObjectName}> <{self.focusObjectDistance}> <{self.focusObjectAngle}>)"
	
	
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
		self.finalReport += f"{s}	\n"
		
	def printFinalReport(self):
		print("Final report:")
		print(self.finalReport)
		
	#----------METODOS DE ACTUALIZACION---------------------------------
	
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
		
	# RECIBE - CLASIFICA - ASIGNA, INFORMACION RECIBIDA DEL SERVIDOR
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
			self.setFocusObject(self.focusObjectName)
		
		elif "hear" in response:
			self.hear = response
			
			if "referee" in response:
				self.gamePhaseUpdate(response)
		
		elif "init" in response:
			
				self.setTeamSide(dataMan.subStrToSpace(response, 1))
				self.setUniformNumber(dataMan.subStrToSpace(response, 2))
				self.setGamePhase(dataMan.subStrToSpace(response, 3))
				self.setGamePhase(dataMan.strTrunc(self.getGamePhase(), ')'))
				
				if self.teamSide == 'l':
					self.setEnemySide('r')
				else:
					self.setEnemySide('l')
					
		elif "error" in response:
			# TODO
			error = "response"
		
		else:
			error = f"ERROR !!! in updateState() unknown response: <{response}>"
			self.errorSumaryUpdate(error)
			self.errorSumaryCount += 1
			#print(error)
			
			return 1
			
		return 0
	
	
			
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
			error = "in setfocusObject() object not in see response"
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
		
	def objectInSight(self, objectName):
		
		if objectName in self.see:
			return True
		else:
			return False
				
	# SETEA LA INFORMACION DEL OBJETO EN CUESTION	
	def setFocusObject(self, objectName):
		objectInfo = self.getObjectInfo(objectName)
		#print(objectInfo)
		
		if objectInfo != None:
			
			#print(f"objectInfo:<{objectInfo}>")
			self.focusObjectName = objectName
			objectDirection = dataMan.subStrToSpace(objectInfo, 0)
			objectAngle = dataMan.subStrToSpace(objectInfo, 1)
			
			# USANDO ESTE METODO ESTAMOS PERDIENDO INFORMACION
			# POR QUE ESTA ECHO PARA PROCESAR COMANDOS COMO EL SIGUIENTE
			# -x -x -x -x
			# NO HE INVESTIGADO QUE SIGNIFICAN LOS SIGUIENTES DATOS
			
			try:
				self.focusObjectDistance = float(objectDirection)
			except Exception as e:
				print(f"failed to convert objectDirection: {objectDirection}.")
				
			try:	
				self.focusObjectAngle = float(objectAngle)
			except Exception as e:
				print(f"failed to convert objectAngle: {objectAngle}.")
			
			return True
		else:
			
			self.focusObjectName = objectName
			self.focusObjectDistance = 0
			self.focusObjectAngle = 0
			return False
				
	# REGRESA TRUE EN CASO DE QUE EL ANGULO DE UN OBJETO
	# ESTE DENTRO DE CIERTO RANGO
	def foAngleInRange(self, mn, mx):
		
		if mn > mx:
			aux = mn
			mn = mx
			mx = aux
		
		if self.focusObjectAngle > mn and self.focusObjectAngle < mx:
			return True
		else:
			return False			
		
	
	# -----METODOS RELATIVOL AL MODELO DE AUDICION "hear"---------------
	
	# REGRESA True SI EL JUGADOR HA ESCUCHADO EL mensaje
	def listen(self, message):
		
		if message in self.hear:
			return True
		else:
			return False
		
	def search_object(self, objectName):
		if not setFocusObject(objectName):
			if self.neckPosition == 0:
				buildCommand("(turn_neck 45)")
				self.neckPosition = 1
				self.fluxphase = "search_object"
			elif self.neckPosition == 1:
				buildCommand("(turn_neck -90)")
				self.neckPosition = 2
				self.fluxphase = "search_object"
			elif self.neckPosition == 2:
				buildCommand("(turn 180)(turn_neck 45)")
				self.neckPosition = 0
				self.fluxphase = "search_object"
			else:
				return 1				# TODO
				# UN EXPECTED ERROR in search_object()
				# INVALID neck_position
	
	def intercept_object(self, objectName):
		return False
