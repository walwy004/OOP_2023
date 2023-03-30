from Vehicle import Vehicle
from Engine import Engine

class Bus(Vehicle):
    def __init__(self, wheelCount, doorCount, VIN, seatCount):
        super().__init__(wheelCount, doorCount, VIN)
        self.__seatCount = seatCount
        self.engine = Engine("Diesel")

    def getSeatCount(self):
        return self.__seatCount
    
    def setSeatCount(self, newSeatCount):
        if newSeatCount < 0:
            self.__seatCount = 0
        elif newSeatCount > 200:
            self.__seatCount = 200
        else:
            self.__seatCount = newSeatCount

    seatCount = property(getSeatCount, setSeatCount)