class Jugador:
	#ATRIBUTOS ASOCIADOS AL ESTADO DEL CUERPO DEL JUGADOR
	sense_body = "0"
	view_mode = "high normal"
	stamina = " 8000 1"
	speed = "0 0"
	head_angle = "0"
	kick = "0"
	dash = "0"
	turn = "0"
	say = "0"
	turn_neck = "0"
	catch = "0"
	move = "0"
	change_view = "0"
	
	#ATRUBUTOS ASOCIADOS AL SERVIDOR
	see = ""
	serverTime = "0"
	role = ""
	equip_name = "test"
	Uniform_name = ""
	
	def __init__(self, role):
		self.role = role
	
	def printBodyState(self):
		print(f"sende_body = {self.sense_body}")
		print(f"view_mode = {self.view_mode}")
		print(f"stamina = {self.stamina}")
		print(f"speed = {self.speed}")
		print(f"head_angle{self.head_angle}")
		print(f"kick = {self.kick}")
		print(f"dash = {self.dash}")
		print(f"turn = {self.turn}")
		print(f"say = {self.say}")
		print(f"turn_neck = {self.turn_neck}")
		print(f"catch = {self.catch}")
		print(f"move = {self.move}")
		print(f"change_view = {self.change_view}")
		
	

	
