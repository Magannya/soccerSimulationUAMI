# PROBABA SEPARAR EN SUS DIFERENTES VARIABLE UN COOMANDO DE FORMA CORRECTA

from Jugador import Jugador

j = Jugador("test")

j.updateState("b'(sense_body 0 (view_mode high normal) (stamina 6354 1) (speed 15 60.5) (head_angle 32) (kick 100) (dash 50) (turn 37.24) (say 1) (turn_neck 45) (catch 1) (move 10) (change_view 14))\x00'")
j.printBodyState()
