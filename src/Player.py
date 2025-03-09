import socket
import dataMan
import sys
import os
import time
import random

from Debug_module import Debug_module

class Player:
	
	# LISTAS sense_body
	senseBody = []
	arm = []
	focus = []
	tackle = []
	foul = []
	
	attrib = []
	
	# LISTA see
	see = []
	
	debugger = None
	dataProcesModule = None
	
	def __init__(self, debugMode):
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
		
		dataProcesModule = Data_process_module(self.attrib, self.dm)
		
	def sayHello(self):
		print("Hello from Player.")
		if self.debugger is not None:
			print("runnig in debugger mode.")
