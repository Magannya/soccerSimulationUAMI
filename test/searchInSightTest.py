def main():
    see = "(see 55 ((f c) 14.255 53.225 0 0) ((f c t) 45.2 21) ((f l t) 60.9 -36) ((f g l t) 45.6 -60) ((f p l t) 39.6 -32) ((f t 0) 49.9 20) ((f t r 10) 53 31) ((f t r 20) 57.4 40) ((f t r 30) 63.4 48) ((f t r 40) 70.1 54) ((f t r 50) 77.5 59) ((f t l 10) 48.9 8) ((f t l 20) 49.9 -3) ((f t l 30) 53 -14) ((f t l 40) 57.4 -23) ((f t l 50) 63.4 -31) ((f l t 10) 51.4 -59) ((f l t 20) 56.3 -49) ((f l t 30) 62.2 -41) ((b) 13.5 53 0 0) ((l t) 44.7 -82))"
    
    objName = "(b)"
    
    lst = searchInSight(see, objName)
    
    if lst is not None:
        print(lst)
        print(lst[1])
    else:
        print("object not in sight")
    
    
    
def searchInSight(see, objName):
        result = []
        index = see.find(objName)
        
        if index < 0:
            return None
        
        c = see[index]
        while c != ')':
            index += 1
            c = see[index]
        
        index += 2
        c = see[index]
        sAux = ""
        while c != " ":
            sAux += c
            index += 1
            c = see[index]
        
        distance = float(sAux)
        
        index += 1
        
        c = see[index]
        sAux = ""
        while c != ' ' and c != ')':
            sAux += c
            index += 1
            c = see[index]
        
        angle = float(sAux)
        
        result.append(distance)
        result.append(angle)
        
        return result
    
if __name__ == "__main__":
    main()
