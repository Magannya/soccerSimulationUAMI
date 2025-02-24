import time
import sys
import os

class Print_manager:
	
	refreshInterval = 0.1
	
	def __init__(self):
		return 0
		
	def say_hello(self):
		print("Hello from Print_manager.")
		
	# SETTERS Y GETTERS-------------------------------------------------
	def set_refresh_interval(self, refreshInterval):
		self.refreshInterval = refreshInterval
	
	def get_refresh_interval(self):
		return self.refreshInterval
