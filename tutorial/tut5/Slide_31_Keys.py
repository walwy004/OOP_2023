class KeyObject:
    def __init__(self):
        pass

dictionary = {}

keyObject = KeyObject()
keyList = [1, 2, 3]
keyDictionary = {1: 10}

dictionary[keyObject] = "An object"
# dictionary[keyList] = "A list."
dictionary[keyDictionary] = "A dictionary."

for key, value in dictionary.items():
    print(f"{key} has a value of: {value}")
