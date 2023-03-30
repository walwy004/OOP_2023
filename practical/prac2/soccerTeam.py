class SoccerTeam:
    def __init__(self, name):
        self.name = name
        self.__won = 0
        self.__lost = 0
        self.__draw = 0
        self.__score = 0
        self.__teamGoals = 0
        self.__oppositionGoals = 0
    
    def addResult(self, teamGoals, oppositionGoals):
        self.__teamGoals += teamGoals
        self.__oppositionGoals += oppositionGoals

        if teamGoals > oppositionGoals:
            self.__won += 1
            self.__score += 3
        elif teamGoals == oppositionGoals:
            self.__draw += 1
            self.__score += 1
        else:
            self.__lost += 1

    def getScore(self):
        return self.__score
    
    def goalDifference(self):
        difference = self.__teamGoals - self.__oppositionGoals
        return difference
    
    def printReport(self):
        report = f"{self.name}: Won: {self.__won} Lost: {self.__lost} Draw: {self.__draw} Team Goals: {self.__teamGoals} "\
                 f"Opposition Goals: {self.__oppositionGoals} Goal difference: {self.goalDifference()} Points: {self.getScore()}"
        print(report)

class Group:
    def __init__(self, name):
        self.name = name
        self.__teams = []
    
    def addTeam(self, team):
        self.__teams.append(team)

    def addMatchResult(self, team, oppositionTeam, teamGoals, oppositionGoals):
        team.addResult(teamGoals, oppositionGoals)
        oppositionTeam.addResult(oppositionGoals, teamGoals)
    
    def printTable(self):
        print(f"Group {self.name}\n\n")
        
        self.__teams.sort(key=lambda team: (team.getScore(), team.goalDifference()), reverse=True)
        for team in self.__teams:
            team.printReport()

seoul = SoccerTeam("Seoul Dynasty")
dalas = SoccerTeam("Dalas Fuel")
florida = SoccerTeam("Florida Mayhem")
losAngeles = SoccerTeam("Los Angeles Valiant")

group = Group("OWL")
group.addTeam(seoul)
group.addTeam(dalas)
group.addTeam(florida)
group.addTeam(losAngeles)

group.addMatchResult(dalas, florida, 3, 0)
group.addMatchResult(seoul, losAngeles, 2, 1)
group.addMatchResult(dalas, seoul, 4, 2)
group.addMatchResult(losAngeles, florida, 1, 6)
group.addMatchResult(losAngeles, dalas, 0, 2)
group.addMatchResult(florida, seoul, 0, 0)

print("\n---------------------------------------------------")
group.printTable()
print("---------------------------------------------------\n") 