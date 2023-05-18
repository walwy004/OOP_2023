# # task 1
# class Base:
#     def printMe(self):
#         print("Calling method printMe() in class Base.")

# class Left(Base):
#     def printMe(self):
#         super().printMe()
#         print("Calling method printMe() in class Left.")

# class Right(Base):
#     def printMe(self):
#         super().printMe()
#         print("Calling method printMe() in class Right.")

# class Sub(Right, Left):
#     def printMe(self):
#         super().printMe()
#         print("Calling method printMe() in class Sub.")

# print(Sub.mro())
# s = Sub()
# s.printMe()

# # task 2
# class Bus:
#     def __init__(self, wheels, seats):
#         self.__wheels = wheels
#         self.__seats = seats

#     def getInfo(self):
#         return f"Number of wheels: {self.__wheels} \nSeats: {self.__seats}"

# class Boat:
#     def __init__(self, screws, lifeJackets):
#         self.__screws = screws
#         self.__lifeJackets = lifeJackets

#     def getInfo(self):
#         return f"Screws: {self.__screws} \nLife Jackets: {self.__lifeJackets}"
    
# class DuckBoat(Bus, Boat):
#     def __init__(self, wheels, seats, screws, lifeJackets, mode):
#         Bus.__init__(self, wheels, seats)
#         Boat.__init__(self, screws, lifeJackets)
#         self.__mode = mode

#     def getInfo(self):
#         bus = Bus.getInfo(self)
#         boat = Boat.getInfo(self)
#         return f"{bus} \n{boat}"

# bus = Bus(4, 40)
# print("== Bus ==")
# print(bus.getInfo())

# boat = Boat(1, 10)
# print("== Boat ==")
# print(boat.getInfo())

# duckboat = DuckBoat(6, 20, 2, 25, "Bus")
# print("== Duck Boat ==")
# print(duckboat.getInfo())

# task 3
class ScoreSheet:
    def __init__(self):
        self.__scores = {}
    
    def addScore(self, key, value):
         self.__scores[key] = value
    
    def getScore(self, key):
        return self.__scores[key]
    
    def getAverageScore(self):
        total = 0
        for value in self.__scores.values():
            total = total + value
        average = total / len(self.__scores)
        return average

scoreSheet = ScoreSheet()
scoreSheet.addScore("OOP", 95)
scoreSheet.addScore("Database", 90)
scoreSheet.addScore("Network", 70)

print("Network Score:", scoreSheet.getScore("Network"))
print("OOP Score:", scoreSheet.getScore("OOP"))
print("Average Score:", scoreSheet.getAverageScore())