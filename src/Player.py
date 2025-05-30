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
        
        gameOver = False
        while not gameOver:
            
            try:
                serverMessage = self.communicationModule.listenServer()
            except TimeoutError:
                print("Connection lost.")
                break
                
            self.dataProcessModule.updateState(serverMessage)
            
            self.printChangePlayMode()
            
            playerResponse = self.randomCommand()
            
            if self.sendCommand(playerResponse) == -1:
                gameOver = True
        
        print("Game Over.")
       
    # ---------------------- COMPLEMENTARY -----------------------------
    def printInfo(self):
        print(self.attrib)
        
    def sendCommand(self, command):
        return self.communicationModule.respondServer(command)
        
    # ----------------------- TEST -------------------------------------
    
    def randomCommand(self):
        dash = f"(dash {random.randint(0, 100)} {random.randint(0, 360)})"
        turn = f"(turn {random.randint(0, 360)})"
        
        if random.randint(1, 2) == 1:
            return dash
        else:
            return turn
        
    # ------------------------- DEBUG ----------------------------------
    def printChangePlayMode(self):
        if self.previousPlayMode != self.playMode:
            print(f"({self.serverTime}) {self.playMode}")
            self.previousPlayMode = self.playMode
