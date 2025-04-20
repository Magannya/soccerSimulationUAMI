import random

def valueInRange(value, ref, rng):
    minValue = ref - rng
    maxValue = ref + rng
    return minValue <= value <= maxValue

def randomDash():
    return random.randint(0, 100)
