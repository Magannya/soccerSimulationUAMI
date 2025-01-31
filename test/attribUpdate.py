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
player.sendCommand("(move -10 0)")
start = time.time()
dif = 0
deltaT = 0.5
cicles = 0
ciclesAUX = 0
serverTime = "0"
prevComm = 0
commInterval = 0
c1 = "(dash 50)"
c2 = "(kick 100 0)"

while not stop:
	
	if player.getServerTimeChange():
		commInterval = time.time() - prevComm
		if dif > 5 and dif < 6:
			player.sendCommand(c2)
		else:
			player.sendCommand(c1)
			
		prevComm = time.time()
		
	player.updateState()
	
	if dif > deltaT:
		os.system('clear')
		player.printBodyState()
		print(f"commInterval: <{commInterval * 1000}>ms")
		deltaT = dif + 0.5

	dif = time.time() - start
	if dif > 30:
		break
		
player.printErrorSumary()
player.bye()
