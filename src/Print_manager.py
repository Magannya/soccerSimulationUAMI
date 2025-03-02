import time
import sys
import os

class Print_manager:
	
	REFRESH_INTERVAL = 0.1
	DINAMIC_ON_SCREEN_TIME = 3
	staticQueue = ""
	dinamicQueue = []
	screenTimeQueue = []
	lastRefresh = 0
	
	def __init__(self):
		print("Print_amager init")
		
	def sayHello(self):
		print("Hello from Print_manager.")
		
	# SETTERS Y GETTERS-------------------------------------------------
	def setRefreshInterval(self, refreshInterval):
		self.REFRESH_INTERVAL = refreshInterval
	
	def getRefreshInterval(self):
		return self.refreshInterval
	
	def dPrintAppend(message):
		self.dinamicQueue.append(message)
		self.screenTimeQueue.append(time.time())
