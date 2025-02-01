import sys
import os
import time

src_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src'))
sys.path.insert(0, src_dir)

from Jugador import Jugador

gol = False

p = Jugador("goleador")
p.sendCommand("(init golTest (version 7))")
p.sendCommand("(move -10 0)")
p.printResponse()
start = time.time()
deltaT = 1
t = 0
while True:
	
	p.updateState()
	p.setObjectFocus("(b)")
	
	if t > deltaT:
		os.system('clear')
		p.printBodyState()
		p.printFocusObject()
		deltaT = t + 0.5
	
	
	if t < 0.4:
		p.sendCommand("(kick 100 0)")
	else:
		p.sendCommand(f"(dash 50)")
	
	
	t = time.time() - start
	if t > 30:
		break

p.bye()
p.printErrorSumary()
