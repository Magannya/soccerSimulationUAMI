from .dataMan import *
from .fieldObject import Field_Object

class Data_process_module:
    
    # LISTAS see
    
    BODY_NAMES = [
    "view_mode",
    "stamina",
    "speed",
    "head_angle",
    "kick",
    "dash",
    "turn",
    "say",
    "turn_neck",
    "catch",
    "move",
    "change_view",
    "change_focus",
    "collision",
    "focus_point"
    ]
    
    ARM_NAMES = [
    "movable",
    "expires",
    "target",
    "count"
    ]
    
    FOCUS_NAMES = [
    "target",
    "count"
    ]
    
    TACKLE_NAMES = [
    "expires",
    "count"
    ]
    
    FOUL_NAMES = [
    "charged",
    "card"
    ]
    
    
    
    def __init__(self, playerAttrib, dm, player):
        
        debugModule = None
        
        # LISTAS sense_body
        self.senseBody = []
        self.arm = []
        self.focus = []
        self.tackle = []
        self.foul = []
        
        self.attrib = []
        self.debugModule = dm
        
        # LISTAS sense_body
        self.senseBody = playerAttrib[0]
        self.arm = playerAttrib[1]
        self.focus = playerAttrib[2]
        self.tackle = playerAttrib[3]
        self.foul = playerAttrib[4]
        #self.see = playerAttrib[5]
        
        self.player = player
        
        self.sayHello()
        print(self.player.see)
        #print("Data_process_module init.")
        
    def sayHello(self):
        print("Hello from Data_process_module")
        
    # SETTERS Y GETTERS ------------------------------------------------
    def setSenseBody(self, senseBody):
        self.player.senseBody = senseBody
        
    def getSenseBody(self):
        return self.player.senseBody
        
    def getStamina(self, i):
        return self.player.senseBody[1][i]
    
    def setStamina(self, i, value):
        self.player.senseBody[1][i] = value
    
    # MAIN -------------------------------------------------------------
    
    def updateState(self, serverMessage):
        if "sense_body" in serverMessage:
            self.senseBodyUpdate(serverMessage)
            # TODO
            
        elif "see" in serverMessage:
            if self.player.playMode != "before_kick_off":
                self.seeUpdate(serverMessage)
            # TODO
            
        elif "hear" in serverMessage:
            #print("Data_Process_Module.hearUpdate(): ", end = "")
            self.hearUpdate(serverMessage)
            
        else:
            pass
    # COMPLEMENTARY ----------------------------------------------------
    
    def printLists(self):
        print(self.player.senseBody)
        print(self.arm)
        print(self.player.focus)
        print(self.tackle)
        print(self.foul)
        print(self.see)
    
    def senseBodyUpdate(self, serverMessage):
        # ACTUALIZACION DEL BLOQUE senseBody
        self.player.serverTime = subStrIS(serverMessage, 0, 1)
        strIndex = serverMessage.find("view_mode")
        self.player.senseBody[0][1] = subStrIS(serverMessage, strIndex, 1)
        self.player.senseBody[0][2] = subStrIS(serverMessage, strIndex, 2)
        
        strIndex = serverMessage.find("stamina")
        self.player.senseBody[1][1] = subStrIStoFloat(serverMessage, strIndex, 1)
        self.player.senseBody[1][2] = subStrIStoFloat(serverMessage, strIndex, 2)
        self.player.senseBody[1][3] = subStrIStoFloat(serverMessage, strIndex, 3)
        
        strIndex = serverMessage.find("speed")
        self.player.senseBody[2][1] = subStrIStoFloat(serverMessage, strIndex, 1)
        self.player.senseBody[2][2] = subStrIStoFloat(serverMessage, strIndex, 2)
        
        i = 3
        while i < 12:
            strIndex = serverMessage.find(self.BODY_NAMES[i])
            self.player.senseBody[i][1] = subStrIStoFloat(serverMessage, strIndex, 1)
            i += 1
        
        strIndex = serverMessage.find("collision")
        self.player.senseBody[12][1] = subStrIS(serverMessage, strIndex, 1)
        
        strIndex = serverMessage.find("focus_point")
        self.player.senseBody[13][1] = subStrIStoFloat(serverMessage, strIndex, 1)
        self.player.senseBody[13][2] = subStrIStoFloat(serverMessage, strIndex, 2)
        
        
        # ACTUALIZACION DEL BLOQUE arm
        strIndex = serverMessage.find("movable")
        self.player.arm[0][1] = subStrIStoFloat(serverMessage, strIndex, 1)
        
        strIndex = serverMessage.find("expires")
        self.player.arm[1][1] = subStrIStoFloat(serverMessage, strIndex, 1)
        
        strIndex = serverMessage.find("target")
        self.player.arm[2][1] = subStrIStoFloat(serverMessage, strIndex, 1)
        self.player.arm[2][2] = subStrIStoFloat(serverMessage, strIndex, 2)
        
        strIndex = serverMessage.find("count")
        self.player.arm[3][1] = subStrIStoFloat(serverMessage, strIndex, 1)
        
        
        # ACTUALIZACION DEL BLOQUE focus
        # ESTA VARIABLE TARGET PODRIA CAMBIAR O UMENTAR DE PARAMETROS
        strIndex = findForward(serverMessage, strIndex+1, "target")
        self.player.focus[0][1] = subStrIS(serverMessage, strIndex, 1)
        
        strIndex = findForward(serverMessage, strIndex, "count")
        self.player.focus[1][1] = subStrIStoFloat(serverMessage, strIndex, 1)
        
        # ACTUALIZACION DEL BLOQUE tackle
        strIndex = findForward(serverMessage, strIndex, "expires")
        self.player.tackle[0][1] = subStrIStoFloat(serverMessage, strIndex, 1)
        
        strIndex = findForward(serverMessage, strIndex, "count")
        self.player.tackle[1][1] = subStrIStoFloat(serverMessage, strIndex, 1)
        
        # ACTUALIZACION DEL BLOCKE foul
        strIndex = findForward(serverMessage, strIndex, "charged")
        self.player.foul[0][1] = subStrIStoFloat(serverMessage, strIndex, 1)
        
        strIndex = findForward(serverMessage, strIndex, "card")
        self.player.foul[1][1] = subStrIS(serverMessage, strIndex, 1)
        
    def hearUpdate(self, serverMessage):
        self.player.serverTime = subStrIS(serverMessage, 0, 1)
        self.player.previousPlayMode = self.player.playMode
        self.player.playMode = subStrIS(serverMessage, 0, 3)
        
    def seeUpdate(self, serverMessage):
        serverTime = ""
        i = 5
        c = serverMessage[i]
        
        # ESTE BLOQUE ESTA DEDICADO A ACTUALIZAR EL player.serverTime
        # DEBIDO A LA EXISTENCIA DE COMANDOS COMO: "(see 0)" QUE NO 
        # TIENEN UNA CANTIDAD DE OBJETOS VISIBLES
        while c != ' ':
            serverTime += c
            i += 1
            c = serverMessage[i]
            if c == ')':
                self.player.serverTime = serverTime
                self.player.see.clear()
                return 0
        
        nameLst = []
        
        # AVANZAR HASTA EN CONTRAR EL CARACTER '('
        # QUE REPRESENTA EL INICIO DE UN OBJETO EN EL CAMPO
        while c != '(':
            i += 1
            c = serverMessage[i]
        
        i += 1
        c = serverMessage[i]
        
        # INICIO DEL CIBLO WHILE QUE OBTENDRA TODOS LOS OBJETOS DEL CAMPO
        cicles = 0
        flag = True
        while flag:
            # OBTENER EL NOMBRE
            name = ""
            while c != ')':
                name += c
                i += 1
                c = serverMessage[i]
            c = serverMessage[i]
            name += c
            i += 1
            c = serverMessage[i]
            
            # ESTA LISTA SERVIRA PARA PUGAR LA LISTA see
            
            nameLst.append(name)
            
            # OBTENER EL ATRIBUTO DISTANCIA
            distanceString = ""
            i += 1
            c = serverMessage[i]
            while c != ' ':
                distanceString += c
                i += 1
                c = serverMessage[i]
            
            # OBTENER EL ATRUBUTO ANGULO
            angleString = ""
            i += 1
            c = serverMessage[i]
            while c != ' ' and c != ')':
                angleString += c
                i += 1
                c = serverMessage[i]
            
            # CASTEO DE LAS VARIABLES
            distance = 0
            angle = 0
            try:
                distance = float(distanceString)
            except Exception as e:
                print(f"Unable to cast {distanceString} to float.")
                distance = None
            
            try:
                angle = float(angleString)
            except Exception as e:
                print(f"Unable to cast {angleString} to float.")
                angle = None
            
            # ACTUALIZACION O ASIGNACION
            
            if not self.findFieldObject(name):
                self.player.see.append([name, distance, angle])
                
            else:
                index = self.getFieldObjectIndex(name)
                self.player.see[index][1] = distance
                self.player.see[index][2] = angle
            
            # EN ESTE PUNTO c = ' ' SI EL OBJETO TIENE MAS ATRUBUTOS, O
            # c = ')' SI EL OBJETO YA NO TIENE MAS ATRIBUTOS
            # EN AMBOS CASOS EL CICLO DEBE CONTINUAR PARA BUSCAR EL
            # SIGUIENTE OBJETO PERO SI EL SIGUIENTE CARACTER ES ')'
            # SIGNIFICA QUE ES EL FINAL DEL MENSAJE DEL SERVIDOR
            
            while c != ')':
                i += 1
                c = serverMessage[i]
                
            i += 1
            c = serverMessage[i]
            
            if c == ')':
                flag = False
            else:
                i += 2
                c = serverMessage[i] 
            cicles += 1
        
        # PURGA DE LA LISTA: SE DEBEN ELIMINAR LOS OBJETOS EN EL CAMPO
        # QUE EXISTEN EN LA LISTA player.see PERO NO EN EL MENSAJE DEL SERVIDOR
        self.purgePlayerSee(nameLst)
        
    # RECIBE UN NOMBRE DE OBJETO EN EL CAMPO Y REGRESA EL INDICE
    # DE LA LISTA 
    def findFieldObject(self, name):
        for fo in self.player.see:
            if fo[0] == name:
                return True
        return False
        
    def getFieldObjectIndex(self, name):
        i = 0
        for fo in self.player.see:
            if fo[0] == name:
                return i
            else:
                i += 1
        return -1
        
    # RECIBE UNA LISTA DE NOMBRES Y BUSCA CADA NOMBRE DE LA LISTA 
    # player.see, SI NO SE ENCUENTRA EN LA LISTA DE NOMBRES ES ELIMINADO
    # DE LA LISTA player.see    
    def purgePlayerSee(self, nameLst):
        i = 0
        lenght = len(self.player.see)
        while i < len(self.player.see):
            if not self.player.see[i][0] in nameLst:
                del self.player.see[i]
            else:
                i += 1
