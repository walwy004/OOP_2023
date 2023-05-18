class Bus:
    def __init__(self, wheels, seats):
        self.__wheels = wheels
        self.__seats = seats

    def getInfo(self):
        return f"Number of wheels: {self.__wheels} \nSeats: {self.__seats}"

class Boat:
    def __init__(self, screws, lifeJackets):
        self.__screws = screws
        self.__lifeJackets = lifeJackets

    def getInfo(self):
        return f"Screws: {self.__screws} \nLife Jackets: {self.__lifeJackets}"
    
class DuckBoat(Bus, Boat):
    def __init__(self, wheels, seats, screws, lifeJackets, mode):
        Bus.__init__(self, wheels, seats)
        Boat.__init__(self, screws, lifeJackets)
        self.__mode = mode

    def getInfo(self):
        bus = Bus.getInfo(self)
        boat = Boat.getInfo(self)
        return f"{bus} \n{boat}"

bus = Bus(4, 40)
print("== Bus ==")
print(bus.getInfo())

boat = Boat(1, 10)
print("== Boat ==")
print(boat.getInfo())

duckboat = DuckBoat(6, 20, 2, 25, "Bus")
print("== Duck Boat ==")
print(duckboat.getInfo())