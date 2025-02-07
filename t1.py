# TEST PARA GESTIONAR LA VISTA DE LOS JUGADORES
# BSCAR LA PELOTA Y TRATAR DE ANOTAR GOL

import sys
import os
import time

sys.path.append('./src')

from src.Jugador import Jugador

p = Jugador("goleador")
p.sendCommand("(move -10 0)")

stop = False
inPosition = False

start = time.time()
deltaT = 0
t = 0
turn = 0

while not inPosition:
	
	p.updateState()
	if not inPosition:
		# MOVERSE A LA POSICION
		inView = p.setFocusObject("(b)")
		if inView:
			print("(b) in see")
			command = f"(dash 50 {p.getFocusObjectAngle()})"
			print(command)
			p.sendCommand(command)
			
			if p.getFocusObjectDirection() < 0.4:
				inPosition = True
			
		else:
			print("(b) not found")
			turn += 10
			
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
	if t > 30:
		p.bye()
		break

if inPosition:
	print("success")
else:
	print("fail")
	
p.bye()


