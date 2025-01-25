import rcssConnect
import time

#VARIABLE QUE ALMANCENA LA CADENA, RESPUESTA DEL SERVIDOR EN CADA CICLO
serverResponse = ""

angle = ""
distance = ""

#ESTA FUNCION TOMA LA RESPUESTA DEL SERVIDOR Y BUSCA SI EL JUGADOR
#TIENE A LA VISTALA PELOTA, SI ES EL CASO, ALMACENA EL ANGULO
#EN LA VARIABLE GLOBAL angle.
def angleToBall(response):
	global angle
	global distance
	index = response.find("(B)")
	
	if index == -1:
		angle = "-1"
		distance = "0"
		return -1
	else:
		
		c = response[index]
		ball = "" + c
		breakFlag = True
		
		while c != ')':
			ball = ball + c
			index = index + 1
			c = response[index]
			
			if c == ')' and breakFlag:
				ball = ball + c
				index = index + 1
				c = response[index]
				breakFlag = False
				
		if c == ')':
			ball = ball + ")"
			
		print(ball)
		
		index = 5
		c = ball[index]
		distance = ""
		
		while c != " ":
			distance = distance + c
			index = index + 1
			c = ball[index]
			
		index = index + 1
		c = ball[index]
		angle = ""
	
		while c != ')':
			angle = angle + c
			index = index + 1
			c = ball[index]
			
	print(f"distance = {distance}, angle = {angle}")

#ESTA FUNCION SE UTILIZA APRA ALMACENAR TODAS LAS RESPUESTAS DEL
#SERVIDOR, AL FINAL DEL PROGRAMA SE ESCRIBE LA VARIABLE EN UN 
#ARCHIVO DE TEXTO
def appendResponse(response):
	global serverResponse
	serverResponse = serverResponse + "\n" + response


#EL CLIENTE TERMINA LA EJECUCION DEL PROGRAMA DESPUES DE 
#30 SEGUNDOS
def client():
	global angle
	global distance
	
	f = open("serverResponse.txt", "a")
	rcssConnect.sendCommand("(init etest (version 7))")
	appendResponse(rcssConnect.getResponse())
	
	rcssConnect.sendCommand("(move -10 0)")
	appendResponse(rcssConnect.getResponse())
	
	start = time.time()
	
	flag = False
	dif = 0
	
	start = time.time()
	
	while True:
		cicleResponse = rcssConnect.getResponse()
		appendResponse(cicleResponse)
		
		angleToBall(cicleResponse)
		print(angle)
		
		floatAngle = float(angle)
		floatDistance = float(distance)
		
		#SI LA PELOTA ESTA CERCA INTENTA PATEARLA, CASO CONTRARIO
		#CORRE HACIA ELLA
		if floatAngle != -1:
			if floatDistance < 0.7:
				rcssConnect.sendCommand("(kick 100 45)")
				print("kick")
			else:
				rcssConnect.sendCommand(f"(dash 30 0)")
				print("run")
		else:
			rcssConnect.sendCommand(f"(dash 30 0)")
			print("run")
		end = time.time()
		dif = end - start
		if dif > 30:
			break	
		
	#ESCRIBE EL ARCHIVO DE TEXT Y FINALIZA LA CONEXION CON EL 
	#SERVIDOR
	f.write(serverResponse)
	f.close()
	rcssConnect.bye()
	

if __name__ == "__main__":
	client()
