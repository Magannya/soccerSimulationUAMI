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

p = Jugador("goleador")

def play():
	
	TeamName = input("Team Name: -> ")

	x = random.randint(0, 10)
	y = random.randint(0, 10)

	p.setTeamName(TeamName)
	p.sendCommand(f"(init {TeamName} (version 7))")
	p.sendCommand(f"(move {x} {y})")
	
	p.refreshForce()
	
	p.setFocusObject("(b)")
	
	while not p.listen("goal"):
		
		p.updateState()
		p.refresh()
		
		i = 0
		while i < 360:
			message = "(turn 1)(turn_neck -1)"
			
			if p.objectInSight("(b)"):
				message = "(turn_neck 1)"
			
			p.sendCommand(message)
			i += 1
		
		# BUSCA LA PELOTA
		# antes que nada queiro saber si la posicion de un objeto
		# es relativo al angulo de la cabeza o al angulo del cuerpo
		
		
		# CORRE HACIA LA PELOTA
		# LLEVA LA PELO TA HASTA UNA POSICION DE TIRO
		# PATEA LA PELOTA PARA LOGRAR UN GOL
	
	p.bye()

def searchBall():
	return 0

if __name__ == "__main__":
	play()
