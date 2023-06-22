class Vehicle:
    def __init__(self, type, doors):
        self.type = type
        self.doors = doors
    
    def getDetails(self):
        return f"--Vehicle Details--\nType: {self.type}\nDoors: {self.doors}\n"
    
class Truck(Vehicle):
    def __init__(self, type, doors, drive, maxLoad):
        super().__init__(type, doors)
        self.drive = drive
        self.__maxLoad = maxLoad
    
    def getDetails(self):
        return super().getDetails() + f"Drive: {self.drive}\nMax Load: {self.__maxLoad}kgs"

truck = Truck("Ute", 2, "4WD", 970)
print(truck.getDetails())