teamMates = {"Solder": 76, "Tracker": 26, "HandSoap": 38, "Windowmaker": 33}

if "Solder" in teamMates:
    print("Solder 76 is a team mate!")

teamMates["Somber"] =  40
teamMates["Somber"] = 30
print("Length of the Dictionary: " + str(len(teamMates)))
del teamMates["Tracker"]

for teamMate in teamMates:
    print("Team Member: " + teamMate)

print(teamMates)