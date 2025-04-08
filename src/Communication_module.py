import socket
import dataMan

class Communication_module:
    
    
    
    def __init__(self):
        
        self.remaningResponse = None    
        self.address = "Localhost"
        self.port = 6000
        self.mySocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.timeChange = True
        self.previousTime = 0
        self.debugger = None
        
        print("Comunication module init.")
    
    def sayHello(self):
        print("Hello from Comunication module.")
        
    # SETTERS Y GETTERS ------------------------------------------------
    
    def setRemaningResponse(self, response):
        self.remaningResponse = response    
    
    def getRemaningResponse(self):
        return self.remaningResponse
        
    def setTimeChange(self, value):
        self.timeChange = value
        
    def getTimeChange(self):
        return self.timeChange
        
    def setDebugger(self, debugger):
        self.debugger = debugger
    
    # MAIN -------------------------------------------------------------
    
    # PARA AGENTES > V7 DEBEMOS ACTUALIZAR EL PORT, DADO QUE EL 
    # PORT 6000 ESTA RESERVADO PARA INITS
    def serverInit(self, teamName):
        self.respondServer(f"(init {teamName} (version 18))", False)
        serverMessage, server = self.mySocket.recvfrom(1024)
        self.debugger.saveServerMessage(serverMessage.decode("utf-8"))
        self.updatePort(server[1])
        print(f"communication established at port: {self.port}")
        return True
    
    def listenServer(self):
        serverMessage, server = self.mySocket.recvfrom(1024)
        serverMessage = serverMessage.decode("utf-8")
        self.debugger.saveServerMessage(serverMessage)
        
        self.timeChange = self.checkTimeChange(serverMessage)
        return serverMessage    
        
    
    # DEBEMOS AGREGAR EL CARACTER '\00' O EL SERVIDOR RESPONDERA:
    # (warnin message_not_null_terminated)
    def inGameRespondServer(self, playerResponse):
        
        if self.timeChange:
            if self.remaningResponse is not None:
                self.mySocket.sendto(self.remaningResponse.encode(), (self.address, self.port))
                self.debugger.savePlayerResponse(playerResponse)
                self.remaningResponse = None
            else:
                self.mySocket.sendto(playerResponse.encode(), (self.address, self.port))
                self.debugger.savePlayerResponse(playerResponse)
        else:
            self.remaningResponse = playerResponse
    
    # HAY QUE CONSULTAR EL ESTADO DEL JUEGO PARA SABER SI VAMOS A OCUPAR
    # ESTE METODO O EL METODO DE inGameRespondServer DESDE ESTE MISMO
    # METODO
    def respondServer(self, playerResponse, inGame):
        if inGame:
            self.inGameRespondServer(playerResponse)
        else:
            playerResponse += "\00"
            self.mySocket.sendto(playerResponse.encode(), (self.address, self.port))
            self.debugger.savePlayerResponse(playerResponse) 
            
    # COMPLEMENTARY ----------------------------------------------------
    
    def checkTimeChange(self, serverMessage):
        actualTime = dataMan.subStrToSpace(serverMessage, 1)
        if actualTime != self.previousTime:
            self.previousTime = actualTime
            return True
        else:
            return False
        
    def updatePort(self, newPort):
        self.port = newPort
