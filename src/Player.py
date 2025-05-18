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
        self.playMode = None
        self.serverTime = None
        
        self.dataProcessModule = Data_process_module(self.attrib, self.playMode, self.debugger)
        self.communicationModule = Communication_module(self.debugger)
        self.communicationModule.serverInit("control")
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
        self.communicationModule.serverInit("test")
        
        gameOver = False
        while not gameOver:
            serverMessage = self.communicationModule.listenServer()
            
            self.dataProcessModule.updateState(serverMessage)
            
            playerResponse = self.randomCommand()
            
            self.sendCommand(playerResponse)
       
    # ---------------------- COMPLEMENTARY -----------------------------
    def printInfo(self):
        print(self.attrib)
        
    def sendCommand(self, command):
        
        if self.playMode == "before_kick_off":
            self.communicationModule.respondServer(command, False)
        else:
            self.communicationModule.respondServer(command, True)
        
    # ----------------------- TEST -------------------------------------
    
    def randomCommand(self):
        dash = f"(dash {random.randint(0, 100)} {random.randint(0, 360)})"
        turn = f"(turn {random.randint(0, 360)})"
        
        if random.randint(1, 2) == 1:
            return dash
        else:
            return turn
        
        
