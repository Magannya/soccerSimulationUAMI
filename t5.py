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
import math

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

    data = {'X':0,'Y':0,'A':0, 'B':0, 'si':0}
    
    x = random.randint(0, 10)
    y = random.randint(0, 10)

    p = Player()
    p.communicationModule.serverInit("test")
    p.sendCommand(f"(move {x} {y} )")
    p.sendCommand("(turn 0)")
    
    pygame.event.pump()
    
    ad = 0    
    try:
        # Guadamos los comandos enviados y las respuestas del servidor en un archivo
        with open(os.path.join(os.path.dirname(__file__), 'data.txt'), 'w') as f:
            print("Iniciando el juego... \n", file=f)

            while True:
                pygame.event.pump()

                eje_X = joystick.get_axis(0)
                eje_Y = joystick.get_axis(1)
                angA = math.atan2(-eje_Y, eje_X)

                btna = joystick.get_button(0)  # Botón A

                if btna == 1 and data['A'] == 0:
                    data['A'] = 1
                    command = "(kick 50 0)"
                    p.sendCommand(command)
                    print(f"Enviando comando: {command}\n", file=f)
                    print(f"Estado de p.see: {p.see}\n", file=f)
                    time.sleep(0.1)
                else:
                    data['A'] = 0

                mag = eje_X**2 + eje_Y**2

                # Se especifica un ángulo de más de 0.1 para evitar el ruido
                if mag > 0.1:
                    if ad == 0:  # ángulo inicial
                        command = f"(turn {(math.degrees(angA) +180) % 360 - 180})"
                        p.sendCommand(command)
                        ad = math.degrees(angA) % 360
                        data['si'] = ad
                        print(f"Enviando comando: {command}\n", file=f)
                        print(f"Estado de p.see: {p.see}\n", file=f)
                        continue
                    else:
                        ad = math.degrees(angA) % 360
                else:
                    continue

                # Movimiento con stick
                angcmd = (data['si'] - ad + 180) % 360 - 180

                command = f"(turn {angcmd})"
                p.sendCommand(command)
                print(f"Enviando comando: {command}", file=f)
                print(f"Estado de p.see: {p.see}", file=f)
                time.sleep(0.1)

                command = "(dash 50)"
                p.sendCommand(command)
                print(f"Enviando comando: {command}\n", file=f)
                print(f"Estado de p.see: {p.see}\n", file=f)
                time.sleep(0.1)

                data['si'] = ad

                continue
    except KeyboardInterrupt:
        p.sendCommand("(bye)")
        print("Agente desconectado")
    finally:
        pygame.quit()

if __name__ == "__main__":
    play()

