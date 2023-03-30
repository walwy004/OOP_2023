class Vehicle:
    def __init__(self):
        pass

    def move(self):
        return "Moving.."

class Car(Vehicle):
    def move(self):
        return super().move() + "On the road..."

class Truck(Car):
    def move(self):
        return super().move() + "Holding heavy cargo."

generic = Vehicle()
car = Car()
truck = Truck()

print(generic.move())
print(car.move())
print(truck.move())
