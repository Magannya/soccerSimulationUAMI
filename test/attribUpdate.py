#from src.Jugador import Jugador
import time
import sys
import os


src_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src'))
sys.path.insert(0, src_dir)

from Jugador import Jugador

stop = False

player = Jugador("Goleador")
player.sayHello()
player.sendCommand("(init autest (version 7))")
player.printResponse()
player.sendCommand("(move -10 10)")
start = time.time()
while not stop:
	
	player.updateState()
	player.printBodyState()
	player.sendCommand("(dash 100)")
	
	end = time.time()
	dif = end -  start
	if dif > 15:
		stop = True
player.bye()
