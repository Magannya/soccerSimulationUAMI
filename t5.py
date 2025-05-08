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
import pygame
    
sys.path.append('./src')

from src.Player import Player
from src import dataMan


def play():
    pygame.init()
    pygame.joystick.init()

    if pygame.joystick.get_count() == 0:
        print("Sin control detectado")
        exit()

    joystick = pygame.joystick.Joystick(0)
    joystick.init()

    data = {'X':0,'Y':0,'A':0, 'B':0, 'sd':0}
    i = 0
    
    p = Player(False)
    
    
    while True:
        pygame.event.pump()

        eje_X = joystick.get_axis(0)
        eje_Y = joystick.get_axis(1)

        boton_A = joystick.get_button(0)
        boton_B = joystick.get_button(1)

        
        if joystick.get_button(0) == 1 and data['A'] == 0:
            p.sendCommand("(turn 90)")
        
        data['A'] = joystick.get_button(0)
        data['B'] = joystick.get_button(1)
        data['sd'] = joystick.get_axis(0)
    
if __name__ == "__main__":
    play()
