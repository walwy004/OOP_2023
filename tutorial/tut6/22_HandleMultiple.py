def division(dividor):
    try:
        return 100 / dividor
    except (ZeroDivisionError, TypeError):
        return "Enter a number other than zero!"

def division(dividor):
    try:
        return 100 / dividor
    except ZeroDivisionError:
        return "Should not divide by zero!"
    except TypeError:
        return "Enter a numerical value."

print(division(0))
print(division(50.0))
print(division("uWu XD Nuzzle Nuzzle"))