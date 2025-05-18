# TEST PARA GESTIONAR LA VISTA DE LOS JUGADORES
# BSCAR LA PELOTA Y TRATAR DE ANOTAR GOL
# LA DIFERENCIA ENTRE t1.py Y t2.py ES EL EQUIPO EN EL QUE SE
# INICIALIZAN LOS JUGADORES, ADEMAS UNO TRATARA DE ANOTAR EN LA 

import sys

sys.path.append('./src')

from src.Player import Player

def play():
    p = Player()
    p.start()
    
if __name__ == "__main__":
    play()
