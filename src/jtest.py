# PROBABA SEPARAR EN SUS DIFERENTES VARIABLE UN COOMANDO DE FORMA CORRECTA
import dataMan

s1 = "b'(player_param 8000 (view_mode high normal) (stamina 6354 1) (speed 15 60.5) (head_angle 32) (kick 100) (dash 50) (turn 37.24) (say 1) (turn_neck 45) (catch 1) (move 10) (change_view 14))\x00'"
s2 = "sense_body"

r = dataMan.subStrToNextWhite("player_param", s1)
print(f"<{r}>")

