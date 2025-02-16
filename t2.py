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
	
	
	searchBall()
	runToBall()
	
	print("done...")
	input()
	p.bye()

def searchBall():
	
	p.setFocusObject("(b)")
	
	while not p.objectInSight("(b)"):
		print("object in sight")
		p.refreshForce()
		p.sendCommand("(turn 20)")
		p.updateState()
	
	while not p.foAngleInRange(-5, 5):
		print("angle in range")
		p.refreshForce()
		p.updateState()
		if p.getfoAngle() < 0:
			p.sendCommand("(turn -2)")
		else:
			p.sendCommand("(turn 2)")
		
	return True

def runToBall():
	while p.getfoDistance() > 0.7:
		print("distance")
		p.sendCommand("(dash 50)")
		p.updateState()
		p.refreshForce()
		
		# ESTO ES UN INTENTO DE FUNCION DE FRENADO
		# LO QUE DEBERIAMOS HACER ES UNA FUNCION QUE RECIBA
		# LA DISTANCIA A LA QUE QUEREMOS PARAR, ANALICE LA VELOCIDAD
		# Y DETERMINE CUANTA FUERZA DEBE APLICAR PARA REDUCIR LA 
		# VELOCIDAD HASTA ESE PUNTO
		
		if p.getfoDistance() < 1.5:
			p.sendCommand("(dash -100)")
			
		if not p.foAngleInRange(-5, 5):
			if p.getfoAngle() < 0:
				p.sendCommand("(turn -2)")
			else:
				p.sendCommand("(turn 2)")
	
	p.sendCommand("(dash -50)")

if __name__ == "__main__":
	play()
