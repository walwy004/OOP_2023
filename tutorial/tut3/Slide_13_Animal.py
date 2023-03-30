class Animal:
    def __init__(self, name, age):
        self.__name = name
        self.age = age

    def getName(self):
        return self.__name

    def showDetails(self):
        print("My name is " + self.getName() + " and I am " + str(self.age) + " years old.")


class Fish(Animal):
    pass


class Cat(Animal):
    def meow(self):
        print(self.getName())

fish = Fish("Wanda", 2)
fish.showDetails()

cat = Cat("Meowser", 5)
cat.showDetails()
cat.meow()
