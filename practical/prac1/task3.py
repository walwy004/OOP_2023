from math import pi

def areaOfCircle(radius):
    area = pi*(radius*radius)
    return area

def circlesInRectangles(length, width, radius):
    area = areaOfCircle(radius)
    numberOfCircles = (length*width) / area
    return numberOfCircles

result = circlesInRectangles(100,100,10)
print(result)