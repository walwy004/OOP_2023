# Task 1
# def circlesInRectangles(length, width, area):
#     numberOfCircles = (length*width) / area
#     return numberOfCircles

# result = circlesInRectangles(10,10,100)
# print(result)

# =========================================================

# task 2
# from math import pi

# def areaOfCircle(radius):
#     area = pi*(radius*radius)
#     return area

# result = areaOfCircle(5)
# print(result)

# =========================================================

# task 3
# from math import pi

# def areaOfCircle(radius):
#     area = pi*(radius*radius)
#     return area

# =========================================================

# def circlesInRectangles(length, width, radius):
#     area = areaOfCircle(radius)
#     numberOfCircles = (length*width) / area
#     return numberOfCircles

# result = circlesInRectangles(100,100,10)
# print(result)

# =========================================================

from math import pi

class Rectangle:
    def __init__(self, length, width, radius):
        self.length = length
        self.width = width
        self.radius = radius

    def areaOfCircle(self):
        area = pi*(self.radius*self.radius)
        return area
    
    def numberOfCircles(self):
        area = self.areaOfCircle()
        numberOfCircles = (self.length*self.width) / area
        return numberOfCircles

rectangle1 = Rectangle(100,50,10)
print("Area of circle:", rectangle1.areaOfCircle())
print("Number of circles:", rectangle1.numberOfCircles())