# TEST PARA GESTIONAR LA VISTA DE LOS JUGADORES
# BSCAR LA PELOTA Y TRATAR DE ANOTAR GOL
# LA DIFERENCIA ENTRE t1.py Y t2.py ES EL EQUIPO EN EL QUE SE
# INICIALIZAN LOS JUGADORES, ADEMAS UNO TRATARA DE ANOTAR EN LA 
# PORTERIA IZAQUIERDA Y EL OTRO EN LA DERECHA

# ESTE SCRIPT TERMINA DESPUES DE 60s

import sys
import os
import time
import random

sys.path.append('./src')

from src.Jugador import Jugador
from src import dataMan

while True:
	TeamName = input("TeamName (a)/(b): -> ")
	if TeamName == "a":
		break
	if TeamName == "b":
		break

if TeamName == "a":
	goalSide = "(g r)"
else:
	goalSide = "(g l)"

x = random.randint(0, 10)
y = random.randint(0, 10)

p = Jugador("goleador")
p.sendCommand(f"(init {TeamName} (version 7))")
p.sendCommand(f"(move {x} {y})")

stop = False
inPosition = False

start = time.time()
deltaT = 0
t = 0
turn = 40
movementAngle = 0

while not inPosition:
	
	p.refresh()
	p.updateState()
	if not inPosition:
		# MOVERSE A LA POSICION
		inView = p.setFocusObject("(b)")
		if inView:		
				
			#p.printAppend("(b) in see")
			#print(p.getFocusObjectAll())
			
			if p.getFocusObjectAngle() > movementAngle:
				movementAngle += 5
				
			else:
				movementAngle -= 5
			
			if p.getFocusObjectDirection() < 1:
				
				objectInfo = p.getObjectInfo(goalSide)
				
				if objectInfo != None:
					kickAngle = dataMan.subStrToSpace(objectInfo, 1)
				else:
					kickAngle = None
					
				if kickAngle == None:
					kickAngle = 0
					
				
				command = f"(kick 50 {kickAngle})"
				
			elif p.getFocusObjectDirection() < 2 and p.getFocusObjectDirection() > 1:
				command = f"(dash -1 0)"
				
			else:
				if p.getFocusObjectAngle() < 5 and p.getFocusObjectAngle() > -5:
					turnAngle = p.getFocusObjectAngle() * -1
					command = f"(turn {turnAngle})"
					
				else:
					command = f"(dash 70 {movementAngle})"
			
			#p.printAppend(command)
			p.sendResponse(command)
			
			
		else:
			#p.printAppend("(b) not found")
			#turn += 
			
			if turn > 360:
				turn = 0
				
			
			command = f"(turn {turn})"
			#p.printAppend(command)
			#p.printAppend(f"self.turn: <{p.getTurn()}>")
			
			p.sendResponse(command)
	
	t = time.time() - start
	#p.printAppend(str(t))
	if t > 300:
		p.bye()
		break

if inPosition:
	print("success")
else:
	print("fail")

p.printFinalReport()
p.sendCommand("(bye)")


