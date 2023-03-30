from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name, age, species):
        self.name = name
        self.age = age
        self.species = species

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def cry(self):
        pass

class Dog(Animal):
    def __init__(self, name, age, species):
        super().__init__(name, age, species)

    def move(self):
        return "Running"

    def cry(self):
        return "Woof woof!"

class Cat(Animal):
    def __init__(self, name, age, species):
        super().__init__(name, age, species)

    def move(self):
        return "Leaping"

    def cry(self):
        return "Meow.."

class Cow(Animal):
    def __init__(self, name, age, species):
        super().__init__(name, age, species)

    def move(self):
        return "Walking"

    def cry(self):
        return "Moooo!"

# Raises error!
animal = Animal("Animal", 1, "Unknown")
animals = []
cat = Cat("Meowser", 5, "Sphinx")
dog = Dog("Sir Pawsom", 2, "Shiba Inu")
cow = Cow("Cowcium", 3, "Angus")

animals.append(cat)
animals.append(dog)
animals.append(cow)

for animal in animals:
    print(animal.name, "is a", type(animal).__name__ 
    + " who is " + animal.move() +" *" + animal.cry() + "*")