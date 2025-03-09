import time
import sys
import os

class Print_manager:
	
	REFRESH_INTERVAL = 0.1
	DINAMIC_ON_SCREEN_TIME = 3
	
	staticQueue = []
	dinamicQueue = []
	screenTimeQueue = []
	lastRefresh = 0
	
	def __init__(self):
		print("Print_manager init")
		
	def sayHello(self):
		print("Hello from Print_manager.")
		
	# SETTERS Y GETTERS-------------------------------------------------
	def setRefreshInterval(self, refreshInterval):
		self.REFRESH_INTERVAL = refreshInterval
	
	def getRefreshInterval(self):
		return self.refreshInterval
		
	def setStaticQueue(self, s):
		self.staticQueue = s;
		
	def getStaticQueue(self):
		return self.staticQueue
		
	def setDinamicQueue(self, lst):
		self.dinamicQueue = lst
		
	def getDinamicQueue(self):
		return self.dinamicQueue
		
	def setScreenTimeQueue(self, lst):
		self.screenTimeQueue = lst
	
	def getScreenTimeQueue(self):
		return self.screenTimeQueue
	
	# MAIN--------------------------------------------------------------
	
	def dPrintAppend(self, s):
		self.dinamicQueue.append([s, time.time()])
		 
		 # s DEBE SER UNA LISTA ["name", value]
	def sPrintAppend(self, s):
		self.staticQueue.append(s)
		
	def sRemove(self, name):
		i = 0
		while i < len(self.staticQueue):
			if name in self.staticQueue[i][0]:
				del self.staticQueue[i]
				break	
			i += 1
				
	def refresh(self):
		now = time.time()
		if now > self.lastRefresh + self.REFRESH_INTERVAL:
			os.system('clear')
			self.printSQ()
			self.printDQ(now)
			self.lastRefresh = now
	
	# COMPLEMENTARY-----------------------------------------------------
	
	def printSQ(self):
		for s in self.staticQueue:
			print(s)
			
	def printDQ(self, now):
		i = 0
		for s in self.dinamicQueue:
			if now - s[1] < self.DINAMIC_ON_SCREEN_TIME:
				print(s[0])
			else:
				del self.dinamicQueue[i]
			i += 1
