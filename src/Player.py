import socket
import sys
import os
import time
import random
import pygame
import math

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
            
            self.sendCommand(playerResponse)
        
        print("Game Over.")

    def startStick(self):
        print("wait for communication...")
        try:
            self.communicationModule.serverInit("test")
        except TimeoutError:
            print("Can not connect with server.")
            return -1
        
        try:
            serverMessage = self.communicationModule.listenServer()
        except TimeoutError:
            print("Connection lost.")
            return

        pygame.init()
        try:
            pygame.joystick.init()        
        except pygame.error as e:
            print(f"Error initializing joystick: {e}")
            return

        if pygame.joystick.get_count() == 0:
            print("No joystick detected")
            pygame.QUIT
            return

        joystick = pygame.joystick.Joystick(0)
        joystick.init()
        data = {'X':0,'Y':0,'A':0, 'B':0, 'si':0}
        
        ad = 0 # ángulo de dirección inicial
        x = random.randint(0, 10)
        y = random.randint(0, 10)
        self.sendCommand(f"(move {x} {y} )")
        self.sendCommand("(turn 0)")

        with open(os.path.join(os.path.dirname(__file__), 'data.txt'), 'w') as f:
            print("Iniciando el juego... \n", file=f)
            gameOver = False
            while not gameOver:    
                # Generación manual de comandos con el joystick                        
                try:
                    # Guadamos los comandos enviados y las respuestas del servidor en un archivo
                    # Actualizamos los valores del stick y el estado del jugador
                    self.dataProcessModule.updateState(serverMessage)
                    self.printChangePlayMode()                            
                    pygame.event.pump()

                    eje_X = joystick.get_axis(0)
                    eje_Y = joystick.get_axis(1)
                    angA = math.atan2(-eje_Y, eje_X)

                    btna = joystick.get_button(0)  # Botón A

                    if btna == 1 and data['A'] == 0:
                        data['A'] = 1
                        command = "(kick 50 0)"
                        self.sendCommand(command)
                        print(f"Enviando comando: {command}\n", file=f)
                        print(f"Estado de p.see: {self.see}\n", file=f)
                        time.sleep(0.1)
                    else:
                        data['A'] = 0

                    mag = eje_X**2 + eje_Y**2

                    # Se especifica un ángulo de más de 0.1 para evitar el ruido
                    if mag > 0.1:
                        if ad == 0:  # ángulo inicial
                            command = f"(turn {(math.degrees(angA) +180) % 360 - 180})"
                            self.sendCommand(command)
                            ad = math.degrees(angA) % 360
                            data['si'] = ad
                            print(f"Enviando comando: {command}\n", file=f)
                            print(f"Estado de p.see: {self.see}\n", file=f)
                            continue
                        else:
                            ad = math.degrees(angA) % 360
                    else:
                        continue

                    # Movimiento con stick
                    angcmd = (data['si'] - ad + 180) % 360 - 180

                    command = f"(turn {angcmd})"
                    self.sendCommand(command)
                    print(f"Enviando comando: {command}", file=f)
                    print(f"Estado de p.see: {self.see}", file=f)
                    time.sleep(0.1)

                    command = "(dash 50)"
                    self.sendCommand(command)
                    print(f"Enviando comando: {command}\n", file=f)
                    print(f"Estado de p.see: {self.see}\n", file=f)
                    time.sleep(0.1)

                    data['si'] = ad

                    continue
                except KeyboardInterrupt:
                    self.sendCommand("(bye)")
                    print("Agente desconectado")
                    gameOver = True
                except Exception as e:
                    print(f"An error occurred: {e}")
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
    def printFullState(self):
        pass
    
    def printChangePlayMode(self):
        if self.previousPlayMode != self.playMode:
            print(f"({self.serverTime}) {self.playMode}")
            self.previousPlayMode = self.playMode
