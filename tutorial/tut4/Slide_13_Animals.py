from Slide_12_Animal import Animal

class Dog(Animal):
    def __init__(self, name, age, species):
        super().__init__(name, age, species)

    def cry(self):
        return super().cry() + "Woof woof!"

class Cat(Animal):
    def __init__(self, name, age, species):
        super().__init__(name, age, species)

    def cry(self):
        return super().cry() + "Meow.."

class Cow(Animal):
    def __init__(self, name, age, species):
        super().__init__(name, age, species)

    def cry(self):
        return super().cry() + "Moooo!"

animals = []
cat = Cat("Meowser", 5, "Sphinx")
dog = Dog("Sir Pawsom", 2, "Shiba Inu")
cow = Cow("Cowcium", 3, "Angus")

animals.append(cat)
animals.append(dog)
animals.append(cow)

for animal in animals:
    print(animal.getName(), "is a", type(animal).__name__ + " *" + animal.cry() + "*")