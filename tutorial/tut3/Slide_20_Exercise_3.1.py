class Insect:
    def __init__(self, wingCount, legSize, hasCarapace):
        self.wingCount = wingCount
        self.legSize = legSize
        self.hasCarapace = hasCarapace

    def crawl(self):
        print("Creep creep...")

class Ant(Insect):
    def __init__(self):
        super().__init__(0, "Small", False)


class Grasshopper(Insect):
    def __init__(self):
        super().__init__(4, "Large", True)

    def hop(self):
        print("Hop hop hop...")


class Bee(Insect):
    def __init__(self):
        super().__init__(2, "Small", False)
        self.hasHoney = False

    def collectHoney(self):
        self.hasHoney = True

    def storeHoney(self):
        self.hasHoney = False
