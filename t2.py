# TEST PARA GESTIONAR LA VISTA DE LOS JUGADORES
# BSCAR LA PELOTA Y TRATAR DE ANOTAR GOL
# LA DIFERENCIA ENTRE t1.py Y t2.py ES EL EQUIPO EN EL QUE SE
# INICIALIZAN LOS JUGADORES, ADEMAS UNO TRATARA DE ANOTAR EN LA 
# PORTERIA IZAQUIERDA Y EL OTRO EN LA DERECHA

# ESTE SCRIPT TERMINA DESPUES DE 60s

import sys
import os
import time

sys.path.append('./src')

from src.Jugador import Jugador
from src import dataMan

teamName = "b"


p = Jugador("goleador")
p.sendCommand(f"(init {teamName} (version 7))")
p.sendCommand("(move -10 20)")

stop = False
inPosition = False

start = time.time()
deltaT = 0
t = 0
turn = 40
movementAngle = 0

while not inPosition:
	
	p.updateState()
	if not inPosition:
		# MOVERSE A LA POSICION
		inView = p.setFocusObject("(b)")
		if inView:		
				
			print("(b) in see")
			print(p.getFocusObjectAll())
			
			if p.getFocusObjectAngle() > movementAngle:
				movementAngle += 1
			else:
				movementAngle += -1
			
			if p.getFocusObjectDirection() < 1:
				
				objectInfo = p.getObjectInfo("(g l)")
				
				if objectInfo != None:
					kickAngle = dataMan.subStrToSpace(objectInfo, 1)
				else:
					kickAngle = None
					
				if kickAngle == None:
					kickAngle = 0
					
				print("-----------------------------------------------------")
				command = f"(kick 50 {kickAngle})"
				print(f"obInf: {objectInfo} comm: {command}")
				print("-----------------------------------------------------")
				# inPosition = True
			else:
				command = f"(dash 70 {movementAngle})"
			
			print(command)	
			p.sendCommand(command)
			
			
		else:
			print("(b) not found")
			#turn += 
			
			if turn > 360:
				turn = 0
				
			
			command = f"(turn {turn})"
			print(command)
			print(f"self.turn: <{p.getTurn()}>")
			p.sendResponse(command)
	
	print(t)
	if t > deltaT:
		#os.system('clear')
		#p.printBodyState()
		deltaT = t + 0.5
		
	t = time.time() - start
	if t > 60	:
		p.bye()
		break

if inPosition:
	print("success")
else:
	print("fail")
	
p.bye()


