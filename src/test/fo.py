from Jugador import Jugador

p = Jugador("goleador")

response = "b'(see 0 ((f c t) 6.7 27 0 0) ((f r t) 58.6 3) ((f g r b) 73 37) ((g r) 69.4 32) ((f g r t) 66 27) ((f p r c) 55.7 41) ((f p r t) 45.2 22) ((f t 0) 6.3 -18 0 0) ((f t r 10) 16.1 -7 0 0) ((b) 3.14 6.28)((f t r 20) 26 -4 0 0) ((f t r 30) 36.2 -3) ((f t r 40) 46.1 -2) ((f t r 50) 56.3 -2) ((f r 0) 73.7 30) ((f r t 10) 68.7 23) ((f r t 20) 66 15) ((f r t 30) 64.1 6) ((f r b 10) 79 37) ((f r b 20) 85.6 42))\x00'"

p.setSee(response)
#print(p.getSee())

p.setFocusObject("(b)")

print(p.getFocusObjectAll())

response = "b'(see 0 ((f c t) 6.7 27 0 0) ((f r t) 58.6 3) ((f g r b) 73 37) ((g r) 69.4 32) ((f g r t) 66 27) ((f p r c) 55.7 41) ((f p r t) 45.2 22) ((f t 0) 6.3 -18 0 0) ((f t r 10) 16.1 -7 0 0) ((b) 40 20)((f t r 20) 26 -4 0 0) ((f t r 30) 36.2 -3) ((f t r 40) 46.1 -2) ((f t r 50) 56.3 -2) ((f r 0) 73.7 30) ((f r t 10) 68.7 23) ((f r t 20) 66 15) ((f r t 30) 64.1 6) ((f r b 10) 79 37) ((f r b 20) 85.6 42))\x00'"

p.setSee(response)
p.setFocusObject("(b)")
print(p.getFocusObjectAll())
