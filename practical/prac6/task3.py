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