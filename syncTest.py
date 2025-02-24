import sys
import os
import time
import random
	
sys.path.append('./src')

from src.Jugador import Jugador
from src import dataMan

p = Jugador("goleador", "teamNameTest")

p.hello()

startT = time.time()
byeT = 10

def play():
	
	angle = 0
	
	while not disconnectT():
		p.updateState()
		p.refresh()
	
		if p.getCommandQueue() == None:
			p.sendResponse2(f"(turn {angle})(turn_neck {angle})")
			angle += 1
		else:
			p.sendResponse2(p.getCommandQueue())
			p.setCommandQueue(None)
			angle += 1
		
	return 0
	
	p.bye()
def disconnectT():
	if startT - time.time() > byeT:
		return True
	else:
		return False
	
if __name__ == "__main__":
	play()

