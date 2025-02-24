import socket
import dataMan
import sys
import os
import time
import random

import Debug_module

class Player:
	
	debugger = None
	
	def __init__(self):
		self.debugger = Debug_module()
		
	def say_hello(self):
		print("Hello from Player.")
