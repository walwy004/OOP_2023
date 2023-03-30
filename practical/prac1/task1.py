def circlesInRectangles(length, width, area):
    numberOfCircles = (length*width) / area
    return numberOfCircles

result = circlesInRectangles(10,10,100)
print(result)