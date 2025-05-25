from .dataMan import *

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
    
    
    
    def __init__(self, playerAttrib, playMode, dm):
        
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
        self.see = playerAttrib[5]
        
        self.playMode = playMode
        print("Data_process_module init.")
        
    def sayHello(self):
        print("Hello from Data_process_module")
        sayHello()
        
    # SETTERS Y GETTERS ------------------------------------------------
    def setSenseBody(self, senseBody):
        self.senseBody = senseBody
        
    def getSenseBody(self):
        return self.senseBody
        
    def getStamina(self, i):
        return self.senseBody[1][i]
    
    def setStamina(self, i, value):
        self.senseBody[1][i] = value
    
    # MAIN -------------------------------------------------------------
    
    def updateState(self, serverMessage):
        if "sense_body" in serverMessage:
            self.senseBodyUpdate(serverMessage)
            # TODO
            
        elif "see" in serverMessage:
            print("")
            # TODO
            
        elif "hear" in serverMessage:
            print("hearUpdate")
            self.hearUpdate(serverMessage)
            
        else:
            print("")
        
    # COMPLEMENTARY ----------------------------------------------------
    
    def printLists(self):
        print(self.senseBody)
        print(self.arm)
        print(self.focus)
        print(self.tackle)
        print(self.foul)
        print(self.see)
    
    def senseBodyUpdate(self, serverMessage):
        # ACTUALIZACION DEL BLOQUE senseBody
        strIndex = serverMessage.find("view_mode")
        self.senseBody[0][1] = subStrIS(serverMessage, strIndex, 1)
        self.senseBody[0][2] = subStrIS(serverMessage, strIndex, 2)
        
        strIndex = serverMessage.find("stamina")
        self.senseBody[1][1] = subStrIStoFloat(serverMessage, strIndex, 1)
        self.senseBody[1][2] = subStrIStoFloat(serverMessage, strIndex, 2)
        self.senseBody[1][3] = subStrIStoFloat(serverMessage, strIndex, 3)
        
        strIndex = serverMessage.find("speed")
        self.senseBody[2][1] = subStrIStoFloat(serverMessage, strIndex, 1)
        self.senseBody[2][2] = subStrIStoFloat(serverMessage, strIndex, 2)
        
        i = 3
        while i < 12:
            strIndex = serverMessage.find(self.BODY_NAMES[i])
            self.senseBody[i][1] = subStrIStoFloat(serverMessage, strIndex, 1)
            i += 1
        
        strIndex = serverMessage.find("collision")
        self.senseBody[12][1] = subStrIS(serverMessage, strIndex, 1)
        
        strIndex = serverMessage.find("focus_point")
        self.senseBody[13][1] = subStrIStoFloat(serverMessage, strIndex, 1)
        self.senseBody[13][2] = subStrIStoFloat(serverMessage, strIndex, 2)
        
        
        # ACTUALIZACION DEL BLOQUE arm
        strIndex = serverMessage.find("movable")
        self.arm[0][1] = subStrIStoFloat(serverMessage, strIndex, 1)
        
        strIndex = serverMessage.find("expires")
        self.arm[1][1] = subStrIStoFloat(serverMessage, strIndex, 1)
        
        strIndex = serverMessage.find("target")
        self.arm[2][1] = subStrIStoFloat(serverMessage, strIndex, 1)
        self.arm[2][2] = subStrIStoFloat(serverMessage, strIndex, 2)
        
        strIndex = serverMessage.find("count")
        self.arm[3][1] = subStrIStoFloat(serverMessage, strIndex, 1)
        
        
        # ACTUALIZACION DEL BLOQUE focus
        # ESTA VARIABLE TARGET PODRIA CAMBIAR O UMENTAR DE PARAMETROS
        strIndex = findForward(serverMessage, strIndex+1, "target")
        self.focus[0][1] = subStrIS(serverMessage, strIndex, 1)
        
        strIndex = findForward(serverMessage, strIndex, "count")
        self.focus[1][1] = subStrIStoFloat(serverMessage, strIndex, 1)
        
        # ACTUALIZACION DEL BLOQUE tackle
        strIndex = findForward(serverMessage, strIndex, "expires")
        self.tackle[0][1] = subStrIStoFloat(serverMessage, strIndex, 1)
        
        strIndex = findForward(serverMessage, strIndex, "count")
        self.tackle[1][1] = subStrIStoFloat(serverMessage, strIndex, 1)
        
        # ACTUALIZACION DEL BLOCKE foul
        strIndex = findForward(serverMessage, strIndex, "charged")
        self.foul[0][1] = subStrIStoFloat(serverMessage, strIndex, 1)
        
        strIndex = findForward(serverMessage, strIndex, "card")
        self.foul[1][1] = subStrIS(serverMessage, strIndex, 1)
        
    def hearUpdate(self, serverMessage):
        self.playMode = subStrIS(serverMessage, 0, 3)
        print(self.playMode)
