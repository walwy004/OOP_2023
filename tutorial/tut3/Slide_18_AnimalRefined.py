class Animal:
    def __init__(self, name, age):
        self.__name = name
        self.age = age

    def getName(self):
        return self.__name

    def showDetails(self):
        print("My name is " + self.getName() + " and I am " + str(self.age) + " years old.")


class Fish(Animal):
    def __init__(self, name, age):
        super().__init__("Wanda", 2)


class Cat(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def meow(self):
        print(self.getName())

fish = Fish()
fish.showDetails()

cat = Cat("Meowser", 5, "Sphinx")
cat.showDetails()
cat.meow()
