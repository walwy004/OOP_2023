class PowerOfTenIterable:
    def __iter__(self):
        return PowerOfTenIterator()

class PowerOfTenIterator:
    def __init__(self):
        self.power = 0
        
    def __next__(self):
        if self.power >= 10:
            raise StopIteration()
        
        value = pow(10, self.power)
        self.power += 1
        return value
    
for number in PowerOfTenIterable():
    print(number)