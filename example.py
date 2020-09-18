#Class
class Triangule:
    def __init__(self, width, height, side1, side2, side3):
        self.width = width
        self.height = height
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.area = (width * height) / 2
        self.perimeter  = (side1 + side2 + side3)
    
    def getArea(self):
        return self.area

    def getPerimeter(self):
        return self.perimeter

#Object
w = float(input("Type the width: "))
h = float(input("Type the height: "))
s1 = float(input("Type the side 1: "))
s2 = float(input("Type the side 2: "))
s3 = float(input("Type the side 3: "))

printTriangule = Triangule(w, h, s1, s2, s3)

print("Triangule area is: %s" % printTriangule.getArea())
print("Triangule perimeter is: %s" % printTriangule.getPerimeter())

