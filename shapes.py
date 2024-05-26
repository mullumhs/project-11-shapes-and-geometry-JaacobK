import math

class Shape:
    def area(self):
        pass
    def perimiter(Self):
        pass
class Rectangle(Shape):
    def __init__(self, width, height):
        self.height = height
        self.width = width
    
    def area(self):
        return self.height * self.width
    
    def perimiter(self):
        return 2 * (self.height + self.width)
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimiter(self):
        return 2 * math.pi * self.radius