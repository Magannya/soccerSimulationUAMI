from Data_process_module import Data_process_module
from Debug_module import Debug_module	
from Player import Player


def start():
	senseBody = [
	["view_mode", "high", "normal"],
	["stamina", 0, 100, 0],
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
	["colision", "none"],
	["focus_point", 0, 0],
	]
	
	arm = [
	["movable", 0],
	["expires", 0],
	["target", 0, 0],
	["count", 0],
	]
	
	focus = [
	["target", "none"],
	["count", 0]
	]
	
	tackle = [
	["expires", 0],
	["count", 0]
	]
	
	foul = [
	["charged", 0],
	["card", "none"]
	]
	
	see = []
	
	attrib = [senseBody, arm, focus, tackle, foul, see]
		
	dm = Debug_module()
	
	dp = Data_process_module(attrib, dm)

	dp.sayHello()
	dp.printLists()
	
	updateMessage = "(view_mode hola mundo)(stamina 100 100 100)(speed 15.2 90.9)"
	
	print(dp.getStamina(2))
	
	dp.senseBodyUpdate(updateMessage)
	
	print(dp.getStamina(2))
	
	dp.printLists()
	
	
	
if __name__ == "__main__":
	start()
