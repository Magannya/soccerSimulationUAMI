# TEST PARA GESTIONAR LA VISTA DE LOS JUGADORES
# BSCAR LA PELOTA Y TRATAR DE ANOTAR GOL

import sys
import os
import time

sys.path.append('./src')

from src.Jugador import Jugador

teamName = input("Team Name: -> ")


p = Jugador("goleador")
p.sendCommand(f"(init {teamName} (version 7))")
p.sendCommand("(move -10 0)")

stop = False
inPosition = False

start = time.time()
deltaT = 0
t = 0
turn = 0
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
				command = f"(kick 100 0)"
				# inPosition = True
			else:
				command = f"(dash 50 {movementAngle})"
			
			print(command)	
			p.sendCommand(command)
			
			
		else:
			print("(b) not found")
			turn += 1
			
			if turn > 360:
				turn = 0
				
			
			command = f"(turn {turn})"
			print(command)
			p.sendCommand(command)
	
	print(t)
	if t > deltaT:
		#os.system('clear')
		p.printBodyState()
		deltaT = t + 0.5
		
	t = time.time() - start
	if t > 60:
		p.bye()
		break

if inPosition:
	print("success")
else:
	print("fail")
	
p.bye()


