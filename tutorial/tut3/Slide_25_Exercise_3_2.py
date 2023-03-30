class Animal:
    def __init__(self, name, age):
        self.__name = name
        self.age = age

    def getName(self):
        return self.__name

    def showDetails(self):
        print("My name is " + self.getName() +
              " and I am " + str(self.age) + " years old.")


class Bird(Animal):
    def fly(self):
        print("flap flap")


class Fish(Animal):
    def swim(self):
        print("Wshwhehwh")


class Cat(Animal):
    def meow(self):
        print("Meow...")


def describe(animal):
    if isinstance(animal, Animal):
        print(animal.getName(), "is a", type(animal).__name__)

        if isinstance(animal, Bird):
            animal.fly()
        elif isinstance(animal, Cat):
            animal.meow()
        elif isinstance(animal, Fish):
            animal.swim()
    else:
        print("This is not an animal.")


animalList = [Bird("Tommy", 4), Cat("Tom", 2), Fish("Tommo", 2), "Surely an animal", ]

for animal in animalList:
    describe(animal)
