import sys
import os
import time
import random

sys.path.append('./src')

from src.Player import Player

print(f"{sys.argv[0]}")
print(f"{sys.argv[1:]}")

if "-d" in sys.argv:
	print("debugger is on")
	p = Player(True)
else:
	print("debugger is off")
	p = Player(False)

p.sayHello()
