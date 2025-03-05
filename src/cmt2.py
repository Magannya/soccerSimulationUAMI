from Comunication_module import Comunication_module
import time

cm = Comunication_module()

playerResponse = ""
serverMessage = ""
i = 0
message = ""
while message != "exit":
	message = input()
	cm.respondServer(message)
	print(cm.listenServer())
	i += 1
	
cm.respondServer("(bye)")
print(f"cicles: {i} done.")
