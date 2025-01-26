from src.Jugador import Jugador
import time
import os

stop = False

player = Jugador("Goleador")
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
