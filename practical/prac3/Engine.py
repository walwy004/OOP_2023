class Engine:
    def __init__(self, type):
        self.__type = type
    
    def getType(self):
        return self.__type
    
    def setType(self, newType):
        self.__type = newType
    
    def showDetails(self):
        details = f"The engine is type: {self.getType()}"
        return details