def division(dividor):
    try:
        return 100 / dividor
    except ZeroDivisionError:
        return "Should not divide by zero!"

print(division(0))
print(division(50.0))
print(division("uWu XD Nuzzle Nuzzle"))