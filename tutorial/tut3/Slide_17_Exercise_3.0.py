class Animal:
    def __init__(self, name, age):
        self.__name = name
        self.age = age

    def getName(self):
        return self.__name

    def showDetails(self):
        print("My name is " + self.getName() + " and I am " + str(self.age) + " years old.")


class Bird(Animal):
    def __init__(self, name, age, wingSpan):
        super().__init__(name, age)
        self.wingSpan = wingSpan


class Fish(Animal):
    def swim():
        pass

class Cat(Animal):
    def meow(self):
        print("Meow...")

class Animal:
    def __init__(self, name, age):
        self.__name = name
        self.age = age

    def getName(self):
        return self.__name

    def showDetails(self):
        print("My name is " + self.getName() + " and I am " + str(self.age) + " years old.")


class Insect(Animal):
    def __init__(self, name, age, hasCarapace):
        super().__init__(name, age)
        self.hasCarapace = hasCarapace