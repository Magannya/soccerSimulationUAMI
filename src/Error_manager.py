class Error_manager:
        
    def __init__(self):
        print("Error_manager init.")
        F_FLAG = True
        
    def fileAppend(self, errorMessage):
        with open("debug_file", "a", encoding="utf-8") as file:
            
            errorMessage.replace('\00', '')
            errorMessage += '\n'
            
            if self.F_FLAG:
                file.truncate(0)
                self.F_FLAG = False
                
            file.write(errorMessage)
    
    def sayHello(self):
        print("hello from Error_manager.");
        
