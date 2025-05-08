import socket
import dataMan
import sys
import os
import time
import random

from Debug_module import Debug_module
from Data_process_module import Data_process_module
from Communication_module import Communication_module

#from FSM import FSM

class Player:
    
    def __init__(self, debugMode):
        # LISTAS sense_body
        self.senseBody = []
        self.arm = []
        self.focus = []
        self.tackle = []
        self.foul = []
    
        self.attrib = []
    
        # LISTA see
        self.see = []
    
        self.debugger = None
        self.dataProcesModule = None
        
        if debugMode:
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
        self.communicationModule = Communication_module()
        self.communicationModule.serverInit("control")
        # self.logicModule = FSM(self.attrib, self.see, self.communicationModule)
        self.logicModule = None
        
        
        
    def sayHello(self):
        print("Hello from Player.")
        if self.debugger is not None:
            print("runnig in debugger mode.")
            
            
    #------------------------------MAIN---------------------------------
    
    def start(self):
        print("wait for communication...")
        self.comunicationModule.serverInit()
        
        gameOver = False
        while not gameOver:
            serverMessage = self.communicationModule.listenServer()
            
            self.dataProcessModule.updateState(serverMessage)
            
            playerResponse = self.logicModule.think
            
            if self.playMode != "play_on":
                inGame = True
            else:
                inGame = False
            
            self.communicationModule.respondServer(playerResponse, inGame)
            
            
        
    def printInfo(self):
        self.dataProcessModule.printLists()
        
    def sendCommand(self, command):
        self.communicationModule.respondServer(command, False)
        
        
