import basic_math

def main():
    value = 21
    ref = 15
    rng = 10
    
    print(basic_math.simple_math.valueInRange(value, ref, rng))
    print(basic_math.angle_math.angleInRange(value, 30))

if __name__ == "__main__":
    main()
