import random
exceptionList = [ValueError, TypeError, IndexError, None]

try:
    choice = random.choice(exceptionList)
    print(f"Raising {choice}")
    if choice:
        raise choice("An Error")
except ValueError:
    print("Caught a ValueError")
except TypeError:
    print("Caught a TypeError")
except Exception as e:
    print("Caught some other error: " + (e.__class__.__name__))
else:
    print("This is called if there is no exception.")
finally:
    print("This cleanup code is always called.")