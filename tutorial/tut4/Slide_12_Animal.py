class Animal:
    def __init__(self, name, age, species):
        self.__name = name
        self.age = age
        self.__species = species

    def getName(self):
        return self.__name

    def getSpecies(self):
        return self.__species
    
    def cry(self):
        return "Grrr..."

