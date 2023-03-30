from abc import ABC, abstractmethod

# class Product:
#     count = 0
#     totalPrice = 0.0

#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#         Product.count += 1
#         Product.totalPrice += self.price

#     @classmethod
#     def averagePrice(cls):
#         return Product.totalPrice / Product.count


# Product("Pen", 3.0)
# Product("Notebook", 5.0)
# Product("Eraser", 1.5)
# Product("Pencil", 2.5)
# print("Average product price:", Product.averagePrice())


class Shape(ABC):
    @abstractmethod
    def getArea(self):
        pass

    @abstractmethod
    def draw(self):
        pass


class Square(Shape):
    def __init__(self, width):
        self.__width = width

    def getArea(self):
        return self.__width * self.__width

    def draw(self):
        for i in range(self.__width):
            print("#" * self.__width)


class Triangle(Shape):
    def __init__(self, base, height):
        self.__base = base
        self.__height = height

    def getArea(self):
        return (self.__base * self.__height) / 2

    def draw(self):
        for i in range(self.__height):
            row = int(i * (self.__base / self.__height))
            print("*" * row)
        print("*" * self.__base)


shapes = [Square(4), Triangle(7, 5)]
for shape in shapes:
    print(f'This {type(shape).__name__} has an area of {shape.getArea()}')
    shape.draw()
    print()

# shape = Shape()
# Shape is an abstract class which means it cannot be instantiated directly
