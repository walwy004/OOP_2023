class Insect:
    def __init__(self, name, wingCount, legSize, hasCarapace):
        self.name = name
        self.wingCount = wingCount
        self.legSize = legSize
        self.hasCarapace = hasCarapace
        self.instects = []

    def crawl(self):
        return self.__class__.__name__ + " is Crawling"


class Ant(Insect):
    def __init__(self, name, wingCount, legSize, hasCarapace, isQueen):
        super().__init__(name, wingCount, legSize, hasCarapace)
        self.isQueen = isQueen


class Grasshopper(Insect):
    def __init__(self, name, wingCount, legSize, hasCarapace, jumpHight):
        super().__init__(name, wingCount, legSize, hasCarapace)
        self.jumpHight = jumpHight

    def crawl(self):
        return "Hop hop hop..."


class Bee(Insect):
    def __init__(self, name, wingCount, legSize, hasCarapace, hasHoney):
        super().__init__(name, wingCount, legSize, hasCarapace)
        self.hasHoney = hasHoney

    def crawl(self):
        return super().crawl() + " *Buzzzzzz*"

    def collectHoney(self):
        self.hasHoney = True

    def storeHoney(self):
        self.hasHoney = False

insects = []
grasshopper = Grasshopper("Hopper", 4, "Large", True, 3.0)
bee = Bee("Berry", 2, "Small", False, True)
ant = Ant("Antonic", 2, "Small", False, True)
insect = Insect("Insect", 0, "Small", False)

insects.append(grasshopper)
insects.append(bee)
insects.append(ant)
insects.append(insect)

for insect in insects:
    print(insect.crawl())
