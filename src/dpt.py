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
	["say", 0],
	["turn_neck", 0],
	["catch", 0],
	["move", 0],
	["change_view", 0],
	["change_focus", 0],
	["collision", "none"],
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
	
	serverMessage = "(sense_body 54 (view_mode 1 2) (stamina 3 4 5) (speed 6 7) (head_angle -8) (kick 9) (dash 10) (turn 11) (say 12) (turn_neck 13) (catch 14) (move 15) (change_view 16) (change_focus 17) (arm (movable 18) (expires 19) (target 20 -21) (count 22)) (focus (target none23) (count 24)) (tackle (expires 25) (count 26)) (collision none27) (foul (charged 28) (card none29)) (focus_point 30 31))"
	
	dp.senseBodyUpdate(serverMessage)
	dp.printLists()
	
if __name__ == "__main__":
	start()
