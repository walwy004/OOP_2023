class Mage:
    def __init__(self, health, mana):
        self.health = health
        self.mana = mana
        self.spells = []
    
    def addSpell(self, spell):
        self.spells.append(spell)
    
    def printSpellbook(self):
        spellbookInfo = ""
        for spell in self.spells:
            spellbookInfo += spell 
            spellbookInfo += "\n "
        return spellbookInfo

class DarkMagician(Mage):
    def __init__(self, health, mana, isNecromancer):
        super().__init__(health, mana)
        self.isNecromancer = isNecromancer
        self.curses = []

    def __str__(self):
        return f"Instance of Dark Magician Class: \n {self.printSpellbook()}" 

mage = Mage(100, 250)
print(mage)

darkMagician = DarkMagician(30, 500, True)
darkMagician.addSpell("Dark Pulse")
darkMagician.addSpell("Raise Skeleton")
darkMagician.addSpell("Reap Soul")
print(darkMagician)