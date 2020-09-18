import math

def getArea(radius):
    area = math.pi * radius
    print("The value of the circle is: " + str(area))

radius = int(input("Input the radius of the circle: "))
getArea(radius)