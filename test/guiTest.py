from src.Jugador import Jugador
from lib import rcssConnect
import curses
from curses import wrapper
import time
import socket

addres = "localhost"
port = 6000
socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

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
		i = 0
		rcssConnect.sendCommand("(init etest (version 7))")
		while not stop:
			
			serverResponse = rcssConnect.getResponse()
			p.listenServer(serverResponse)
			stdscr.addstr(0, 0, p.getState())
			stdscr.refresh()
			
		
	finally:
		rcssConnect.bye()

	
curses.wrapper(main)
