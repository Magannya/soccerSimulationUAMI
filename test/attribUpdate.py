import time
import sys
import os


src_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src'))
sys.path.insert(0, src_dir)

from Jugador import Jugador

stop = False

player = Jugador("Goleador")
player.sendCommand("(init autest (version 7))")
player.printResponse()
player.sendCommand("(move -10 10)")
start = time.time()
dif = 0
deltaT = 15

while not stop:
	
	if dif > deltaT:
		os.system('clear')
		player.printBodyState()
		deltaT += 0.5
		
	player.updateState()
	player.sendCommand("(dash 100)")
	
	end = time.time()
	dif = end -  start
	if dif > 30:
		stop = True
player.bye()
