from Data_process_module import Data_process_module
from Debug_module import Debug_module	
from Player import Player


def start():
		
	p = Player(False)
	p.sayHello()
	p.printInfo()
	
if __name__ == "__main__":
	start()
