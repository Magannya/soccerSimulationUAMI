import random
class Logic_Module_Test:
    def __init__(self, player):
        self.lastCommand = None
            
    def think(self):
        see = player.see
        if see.find("b"):
            
        
    #------------------ MOVEMENT ----------------------------------
    def turnNeckRight(self):
        return "(turn_neck 45)"
    def turnNeckLeft(self):
        return "(turn_neck -45)"
    def turnArround(self):
        return "(turn 180)"
    def turnRight(self):
        return "(turn 45)"
    def turnLeft(self):
        return "(turn -45)"
        
    def dashLow(self):
        return f"(dash {random.randint(1, 33)})"
    def dashMid(self):
        return f"(dahs {random.randint(34, 67)})"
    def dashHigh(self):
        return f"(dash {random.randint(68, 100)})"
    def dashFull(self):
        return "(dash 100)"
        
    def kickLow(self):
        return f"(kick {random.randint(0, 33)})"
    def kickMid(self):
        return f"(kick {random.randint(34, 67)})"
    def kickHigh(self):
        return f"(kick {random.randint(68, 100)})"
    def kickFull(self):
        return "(kick 100)"
