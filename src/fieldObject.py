class Field_Object:
    def __init__(self, name, distance, angle):
        self.name = name
        self.distance = distance
        self.angle = angle
        
    def setDistance(self, distance):
        self.distance = distance
    def setAngle(self, angle):
        self.angle = angle
        
    def getName(self):
        return self.name
    def getDistance(self):
        return self.distance
    def getAngle(self):
        return self.angle
