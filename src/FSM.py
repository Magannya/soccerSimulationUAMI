import DataMan
import Random
import basic_math

def FSM:
    def __init__(attrib, see, communication, position):
        self.state = "idle"
        self.attrib = attrib
        self.see = see
        self.communication = communication
        self.position = position
        
        if position == "center mid":
            self.positionRef = "(f c)"
        
        
        print("Finite state machine init.");
    
    def sayHello():
        print("Hello from FSM.")
        
    def run():
        if self.state == "idle":
            self.idle()
        
        elif self.state == "alert":
            self.alert()
        
        elif self.state == "offensive":
            self.offensive()
        
        elif self.state == "attack":
            self.attack()
        
    # ----------------STATES--------------------------------------------
    
    # state 0
    def idle():
        # LOGICA DE ESTADO
        
        lst = self.searchInSight(positionRef)
        
        
        if lst is not None:
        # EL PUNTO DE REFERENCIA ESTA A LA VISTA    
            distance = lst[0]
            angle = lst[1]
            
            
            if distance > 20:
            # EL PUNTO DE REFERENCIA ESTA MUY LEJOS
                
                if basic_math.angle_math.angleInRange(angle, 20)
                    # EL ANGULO AL PUNTO DE REFERENCIA ESTA EN UN 
                    # RANGO ACEPTABLE PARA MOVERSE HACIA EL
                    
                    command = f"dash({self.randomDash()})"
                else:
                    # EL ANGULO AL PUNTO DE REFERENCIA ESTA 
                    # FUERA DEL RANGO PARA MOVERSE HACIA EL
                    command = f"turn({self.randomAngle()})"
            else:
                command = f"turn_neck({self.randomAngle()})"
            
        else:
            # EL PUNTO DE REFERENCIA NO ESTA A LA VISTA
            command = f"turn({self.randomAngle()})"
        
        # LOGICA DE TRANSICION
        if self.ballNear():
            self.state = "alert"
        
        return 0
        
    #state 1
    def alert():
        return 0
        
    # state 2
    def offensive():
        return 0
    
    # state 3
    def attack():
        return 0
        
    # -------------- EVENTS --------------------------------------------
    # EL VALOR 20 DE ESTE METODO ES ARBITRARIO
    def ballNear(self):
        
        lst = self.searchInSight("(b)")
        if lst is not None:
            if lst[0] < 20:
                return True
            else:
                return False
        else:
            return False
    
    #---------------- IDLE METHODS -------------------------------------
    def positionInRange(self):
        lst = searchInSight(self.positionRef)
        if lst is not None:
            if lst[0] < 50:
                return True
            else:
                return False
        else:
            return False
    
    # ---------------Complementary--------------------------------------
    
    # RECIBE COMO PARAMETRO EL NOMBRE DEL OBJETO Y REGRESA UNA LISTA
    # CON SU DISTANCIA Y ANGULO
    # SI EL OBJETO NO ES ENCONTRADO REGRESA None
    def searchInSight(self, objName):
        
        result = []
        index = self.see.find(objName)
        
        if index < 0:
            reutrn None
        
        c = self.see[index]
        while c != ')':
            index += 1
            c = self.see[index]
        
        index += 2
        c = self.see[index]
        sAux = ""
        while c != " ":
            sAux += c
            index += 1
            c = self.see[index]
        
        distance = float(sAux)
        
        index += 1
        
        c = self.see[index]
        sAux = ""
        while c != ' ' and c != ')':
            sAux += c
            index += 1
            c = self.see[index]
        
        angle = float(sAux)
        
        result.append(distance)
        result.append(angle)
        
        return result
        
    def randomAngle(self):
        return random.randint(-360, 360)
    
    def randomDash(self):
        return random.randint(0, 100)
    
    # --------------GETTERS Y SETTERS-----------------------------------
    def printState(self):
        print(f"FSM state: {self.state}")
    

