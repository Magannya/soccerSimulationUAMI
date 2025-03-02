import socket
import dataMan
import sys
import os
import time
import random

from Debug_module import Debug_module

class Player:
	
	debugger = None
	
	def __init__(self, debugMode):
		if debugMode:
			self.debugger = Debug_module()
		
		
	def sayHello(self):
		print("Hello from Player.")
		if self.debugger is not None:
			print("runnig in debugger mode.")
