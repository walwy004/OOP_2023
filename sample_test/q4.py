class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.__speed = 0

    def accelerate(self, acceleration):
        self.__speed += acceleration
        print(f"The {self.make} {self.model} is accelerating. Current speed: {self.__speed} km/h")

    def getSpeed(self):
        return self.__speed
    
    def setSpeed(self, newSpeed):
        self.__speed = newSpeed
    
    speed = property(getSpeed, setSpeed)

class PetrolCar(Car):
    def __init__(self, make, model, fuelType = "Petrol"):
        super().__init__(make, model)
        self.fuelType = fuelType

class ElectricCar(Car):
    def __init__(self, make, model, fuelType = "Electric"):
        super().__init__(make, model)
        self.fuelType = fuelType

class HybridCar(Car):
    def __init__(self, make, model, fuelType):
        super().__init__(make, model)
        self.fuelType = fuelType

    def accelerate(self, acceleration):
        self.speed = 0  # Reset the speed to zero before each acceleration
        if self.fuelType == "Petrol":
            super().accelerate(acceleration)
        elif self.fuelType == "Electric":
            super().accelerate(acceleration + 10)

petrolCar = PetrolCar("Mazda", "3")
petrolCar.accelerate(30)

electricCar = ElectricCar("Honda", "Type R")
electricCar.accelerate(50)

hybridCar = HybridCar("Hyundai", "i30", "Petrol")
hybridCar.accelerate(70)

hybridCar.fuelType = "Electric"
hybridCar.accelerate(70)
