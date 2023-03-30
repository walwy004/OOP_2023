from abc import ABC, abstractmethod   

class Operator(ABC):
    @abstractmethod
    def calculate(self, a, b):
        pass
    
    @abstractmethod
    def get_symbol(self):
        pass

class Calculator:
    def __init__(self):
        self.__operators = []
    
    def register(self, op:Operator):
        self.__operators.append(op)
    
    def calculate(self, symbol, a, b):
        for o in self.__operators:
            if o.get_symbol() == symbol:
                return o.calculate(a, b)
    
class Addition():
    def calculate(self, a, b):
        return a + b
    
    def get_symbol(self):
        return "+"
    
class Substraction():
    def calculate(self, a, b):
        return a - b
    
    def get_symbol(self):
        return "-"
    
class Multiplication():
    def calculate(self, a, b):
        return a*b
    
    def get_symbol(self):
        return "*"

class Division():
    def calculate(self, a, b):
        return a/b
    
    def get_symbol(self):
        return "/"
# MAIN:

c = Calculator()
a = Addition()
c.register(a)
print("Result of 1+2: " + str(c.calculate("+", 1, 2)))
s = Substraction()
c.register(s)
print("Result of 1-2: " + str(c.calculate("-", 1, 2)))
m = Multiplication()
c.register(m)
print("Result of 1*2: " + str(c.calculate("*", 1, 2)))

#print("Is a an instance of Operator?" + str(isinstance(a, Operator)))

if hasattr(a, 'calculate') and callable(a.calculate):
    print("Method 'calculate()' is available in oject a.")
