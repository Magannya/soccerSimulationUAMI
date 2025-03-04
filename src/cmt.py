from Comunication_module import Comunication_module
import time

cm = Comunication_module()

playerResponse = ""
serverMessage = ""

cm.respondServer("(init cmt (version 7))")
playerResponse = "(turn 180)"
input()
cm.respondServer("(move -10 10)")

enlapsedTime = 0
i = 0

input()
start = time.time()
while enlapsedTime < 10:
	#print(cm.listenServer())
	cm.listenServer()
	cm.respondServer(playerResponse)
	
	enlapsedTime = time.time() - start
	i += 1
cm.respondServer("(bye)")
print(f"cicles: {i}done.")
