from Engine import Engine

class Vehicle:
    def __init__(self, wheelCount, doorCount, VIN):
        self.wheelCount = wheelCount
        self._doorCount = doorCount
        self.__VIN = VIN
        self.engine = Engine("")

    def getVIN(self):
        return self.__VIN
    
    def setVIN(self, newVIN):
        self.__VIN = newVIN
    
    vin = property(getVIN, setVIN)

    def showEngineDetails(self):
        return self.engine.showDetails()