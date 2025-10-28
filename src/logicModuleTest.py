import random
class Logic_Module_Test:
    def __init__(self, player):
        self.lastCommand = None
        self.player = player
            
    def think(self):
        ball = self.findInPlayerSee("(b)")
        print(ball)
        if ball is not None:
            ballDistance = ball[1]
            ballAngle = ball[2]
            
            if self.checkAngleTo(ballAngle):
                return self.correctBodyAngleTo(ballAngle)
            
            if ballDistance >= 30:
                return self.dashHigh()
            elif 10 < ballDistance < 30:
                return self.dashMid()
            elif ballDistance <= 10:
                if self.ballIsKickable(ballDistance):
                    return self.kickMid()
                else:
                    return self.dashMid()
            
        else:
            return self.turnRight()
            
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
        return f"(dash {random.randint(34, 67)})"
    def dashHigh(self):
        return f"(dash {random.randint(68, 100)})"
    def dashFull(self):
        return "(dash 100)"
        
    def kickLow(self):
        return f"(kick {random.randint(0, 33)} )"
    def kickMid(self):
        return f"(kick {random.randint(34, 67)} 0)"
    def kickHigh(self):
        return f"(kick {random.randint(68, 100)})"
    def kickFull(self):
        return "(kick 100)"
        
    #--------------COMPLEMENTARY--------------------------------
    def findInPlayerSee(self, fieldObjectName):
        for fieldObject in self.player.see:
            #print(self.player.see[0])
            if fieldObject[0] == fieldObjectName:
                return fieldObject
        return None
        
    #Esta clase de funciones deberia estar directamente relacionada
    #con un systema de navegacion
    def ballIsKickable(self, ballDistance):
        if 0 <= ballDistance <= 0.7:
            return True
        else:
            return False
            
    def checkAngleTo(self, objectAngle):
        margin = 20
        if -margin <= objectAngle <= margin:
            return True
        else:
            return False
            
    def correctBodyAngleTo(self, objectAngle):
        return f"(turn {-objectAngle})"
