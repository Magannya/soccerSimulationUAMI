import random

def angle_difference(angle1, angle2):
    return angleq1 - angle2
    
def randomAngleMnMx(mn, mx):
    return Random.randint(mn, mx)
    
def randomAngleRef(ref):
    refMin = ref - 30
    refMax = ref + 30
    return Random.randint(refMin, refMax)
    
def angleInRange(angle, toleranceRange):
    return -toleranceRange <= angle <= toleranceRange
    
def randomAngle():
    return random.randint(-360, 360)
    
def greeting():
    print("hello from angle_math.")
