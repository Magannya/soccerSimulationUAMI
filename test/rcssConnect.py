#ESTA LIBRERIA DEFINE FUNCIONES PARA MANDAR COMANDOS AL SERVIDOR
#Y RECIBIR RESPUESTAS

import socket

addres = "localhost"
port = 6000
socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def sendCommand(message):
	socket.sendto(message.encode(), (addres, port))
	
def printResponse():
	response, server = socket.recvfrom(1024)
	print(f"{response.decode()}")
	
def getResponse():
	response, server = socket.recvfrom(1024)
	raw_response = r'{}'.format(response)
	return raw_response

def bye():
	sendCommand("(bye)")
	socket.close()
