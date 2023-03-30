class Vehicle:
    def __init__(self):
        pass

    def move(self):
        return "Moving.."


class Car(Vehicle):
    def move(self):
        return f"{super().move()} on the road..."


class Truck(Car):
    def move(self):
        return f"{super().move()} Holding heavy cargo."


vehicle = Vehicle()
car = Car()
truck = Truck()

print(vehicle.move())
print(car.move())
print(truck.move())
