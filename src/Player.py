import socket
import sys
import os
import time
import random

from .Debug_module import Debug_module
from .Data_process_module import Data_process_module
from .Communication_module import Communication_module

#from FSM import FSM

class Player:
    
    
    def __init__(self):
        # LISTAS sense_body
        self.senseBody = []
        self.arm = []
        self.focus = []
        self.tackle = []
        self.foul = []
    
        self.attrib = []
    
        # LISTA see
        self.see = []
    
        self.dataProcesModule = None
        
        self.debugger = Debug_module()
            
        self.senseBody = [
        ["view_mode", "high", "normal"],
        ["stamina", 0, 0, 0],
        ["speed", 0, 0],
        ["head_angle", 0],
        ["kick", 0],
        ["dash", 0],
        ["turn", 0],
        ["say", 0],
        ["turn_neck", 0],
        ["catch", 0],
        ["move", 0],
        ["change_view", 0],
        ["change_focus", 0],
        ["collision", "none"],
        ["focus_point", 0, 0],
        ]
        
        self.arm = [
        ["movable", 0],
        ["expires", 0],
        ["target", 0, 0],
        ["count", 0]
        ]
        
        self.focus = [
        ["target", "none"],
        ["count", 0],
        ]
        
        self.tackle = [
        ["expires", 0],
        ["count", 0],
        ]
        
        self.foul = [
        ["charged", 0],
        ["card", "none"]
        ]
        
        self.attrib = (self.senseBody, self.arm, self.focus, self.tackle, self.foul, self.see)
        
        # atributo para determinar que posicion va a jugar
        self.position = None
        
        #GAME STATUS ATTRIBUTES, de momento el modulo de procesamiento
        # de datos no actualiza estos atributos
        self.playMode = "before_kick_off"
        self.serverTime = None
        self.previousPlayMode = None
        
        self.dataProcessModule = Data_process_module(self.attrib, self.debugger, self)
        self.communicationModule = Communication_module(self.debugger, self)
        # self.logicModule = FSM(self.attrib, self.see, self.communicationModule)
        self.logicModule = None
        
        
    def sayHello(self):
        print("Hello from Player.")
        if self.debugger is not None:
            print("runnig in debugger mode.")
            
            
    #------------------------------MAIN---------------------------------
    
    # METODO PRINCIPAL PARA INICIAR LA INTERACCION CON EL SERVIDOR
    def start(self):
        print("wait for communication...")
        try:
            self.communicationModule.serverInit("test")
        except TimeoutError:
            print("Can not connect with server.")
            return -1
        
        print("")
        print(f"{self.senseBody[0][0]}\t{self.senseBody[0][1]}\t{self.senseBody[0][2]}")
        print(f"{self.senseBody[1][0]}\t\t{self.senseBody[1][1]}\t{self.senseBody[1][2]}\t{self.senseBody[1][3]}")
        print(f"{self.senseBody[2][0]}\t\t{self.senseBody[2][1]}\t{self.senseBody[2][2]}")
        print(f"{self.senseBody[3][0]}\t{self.senseBody[3][1]}")
        print(f"{self.senseBody[4][0]}\t\t{self.senseBody[4][1]}")
        print(f"{self.senseBody[5][0]}\t\t{self.senseBody[5][1]}")
        print(f"{self.senseBody[6][0]}\t\t{self.senseBody[6][1]}")
        print(f"{self.senseBody[7][0]}\t\t{self.senseBody[7][1]}")
        print(f"{self.senseBody[8][0]}\t{self.senseBody[8][1]}")
        print(f"{self.senseBody[9][0]}\t\t{self.senseBody[9][1]}")
        print(f"{self.senseBody[10][0]}\t\t{self.senseBody[10][1]}")
        print(f"{self.senseBody[11][0]}\t{self.senseBody[11][1]}")
        print(f"{self.senseBody[12][0]}\t{self.senseBody[12][1]}")
        print(f"{self.senseBody[13][0]}\t{self.senseBody[13][1]}")
        print(f"{self.senseBody[14][0]}\t{self.senseBody[14][1]}")
        print(f"server time:\t{self.serverTime}")
        print(f"play mode:\t{self.playMode}")
        
        gameOver = False
        while not gameOver:
            
            try:
                serverMessage = self.communicationModule.listenServer()
            except TimeoutError:
                print("Connection lost.")
                break
                
            self.dataProcessModule.updateState(serverMessage)
            
            playerResponse = self.randomCommand()
            
            self.sendCommand(playerResponse)
            
            self.printFullState()
        
        print("Game Over.")
       
    # ---------------------- COMPLEMENTARY -----------------------------
    def printInfo(self):
        print(self.attrib)
        
    def sendCommand(self, command):
        return self.communicationModule.respondServer(command)
        
    # ----------------------- TEST -------------------------------------
    
    def randomCommand(self):
        
        r = random.randint(1, 3) 
        
        if  r == 1:
            return f"(dash {random.randint(0, 100)} {random.randint(0, 360)})"
        elif r == 2:
            return f"(turn {random.randint(0, 360)})"
        else:
            return f"(turn_neck {random.randint(-90, 90)})"
        
    # ------------------------- DEBUG ----------------------------------
    def printFullState(self):
        for i in range(0, 17):
            print("\r" + "\033[2K", end = "")
            print("\033[1A", end = "")
        print(f"{self.senseBody[0][0]}\t{self.senseBody[0][1]}\t{self.senseBody[0][2]}")
        print(f"{self.senseBody[1][0]}\t\t{self.senseBody[1][1]}\t{self.senseBody[1][2]}\t{self.senseBody[1][3]}")
        print(f"{self.senseBody[2][0]}\t\t{self.senseBody[2][1]}\t{self.senseBody[2][2]}")
        print(f"{self.senseBody[3][0]}\t{self.senseBody[3][1]}")
        print(f"{self.senseBody[4][0]}\t\t{self.senseBody[4][1]}")
        print(f"{self.senseBody[5][0]}\t\t{self.senseBody[5][1]}")
        print(f"{self.senseBody[6][0]}\t\t{self.senseBody[6][1]}")
        print(f"{self.senseBody[7][0]}\t\t{self.senseBody[7][1]}")
        print(f"{self.senseBody[8][0]}\t{self.senseBody[8][1]}")
        print(f"{self.senseBody[9][0]}\t\t{self.senseBody[9][1]}")
        print(f"{self.senseBody[10][0]}\t\t{self.senseBody[10][1]}")
        print(f"{self.senseBody[11][0]}\t{self.senseBody[11][1]}")
        print(f"{self.senseBody[12][0]}\t{self.senseBody[12][1]}")
        print(f"{self.senseBody[13][0]}\t{self.senseBody[13][1]}")
        print(f"{self.senseBody[14][0]}\t{self.senseBody[14][1]}")
        print(f"server time:\t{self.serverTime}")
        print(f"play mode:\t{self.playMode}")
    
    def printChangePlayMode(self):
        if self.previousPlayMode != self.playMode:
            print(f"({self.serverTime}) {self.playMode}")
            self.previousPlayMode = self.playMode
