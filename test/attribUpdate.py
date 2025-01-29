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
deltaT = 0.5
cicles = 0
ciclesAUX = 0
serverTime = "0"

while not stop:
	
	if serverTime != player.getServerTime():
		if cicles > ciclesAUX:
			ciclesAUX = cicles
			cicles = 0
	
	serverTime = player.getServerTime()
		
	if dif > deltaT:
		os.system('clear')
		player.printBodyState()
		
		deltaT += 0.5
	response = player.getResponse()
	
	# SINCRONIZAR TIEMPO DEL SERVIDOR
	player.serverTimeSync(response)
	
	# ACTUALIZAR LOS DATOS DEL CUERPO DEL JUGADOR
	# SOLO CUANDO EL COMANDO DE RESPUESTA ES sense_body
	if "sense" in response:
		player.updateState(response)
	
	player.sendCommand("(dash 100)")
	
	end = time.time()
	dif = end -  start
	if dif > 30:
		stop = True
	cicles += 1
	
print(f"ciclesAUX: {ciclesAUX}")
player.bye()
