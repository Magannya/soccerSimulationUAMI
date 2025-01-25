#ARCHIVO DEDICADO A INICIALIZAR UN AGENTE

from lib import rcssConnect
from src.Jugador import Jugador
import curses

def main():
	player = Jugador("delantero")
	player.printBodyState()
	rcssConnect.sendCommand("(init test (version 15))")
	rcssConnect.printResponse()
	
	while True:
		rcssConnect.printResponse()
	
	rcssConnect.bye()
	
if __name__ == "__main__":
	main()
