import rcssConnect
from src.Jugador import Jugador
from lib import rcssConnect
import curses
from curses import wrapper
import time

def main(stdscr):
	
	curses.curs_set(0)
	curses.start_color()
	
	curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
	
	stdscr.bkgd(' ', curses.color_pair(1))
	
	stdscr.addstr("Prueba de interfaz grafica para un jugador.\n presiona una tecla para iniciar.", curses.color_pair(1))
	
	stdscr.refresh()
	stdscr.getch()
	
	try:
		
		stop = False;
		p = Jugador("goleador")
		
		#BUCLE INFINITO AQUI	
		while stop:
			
			serverResponse = rcssConnect.getResponse()
			p.listenServer(serverResponse)
			
		
	finally:
		rcssConnect.bye()

	
curses.wrapper(main)
