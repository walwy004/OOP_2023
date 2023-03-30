class Sorter:
    def __init__(self, string, number, sortByNum):
        self.string = string
        self.number = number
        self.sortByNum = sortByNum
    
    def __lt__(self, sortObject):
        if self.sortByNum:
            return self.number < sortObject.number
        return self.string < sortObject.string
    
    def __repr__(self):
        return f"{self.string} : {self.number}"

sorterA = Sorter("A", 4, True)
sorterB = Sorter("B", 3, True)
sorterC = Sorter("C", 2, True)
sorterD = Sorter("D", 1, True)

listToSort = [sorterA, sorterB, sorterC, sorterD]
listToSort.sort()
print(listToSort)

for sorter in listToSort:
    sorter.sortByNum = False

listToSort.sort()
print(listToSort)

