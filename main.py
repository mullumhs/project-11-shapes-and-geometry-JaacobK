from shapes import Shape, Rectangle, Circle

print("Welcome to Shapes and Geometry")
choice = input("type\n1. For rectangle\n2. For circle\n")
if choice == "1":
    width = int(input("Please enter the width of the rectangle\n"))
    height = int(input("Please enter the hieght of the rectangle\n"))
    rectangle = Rectangle(width, height)
    print(f"Your rectangles area is {rectangle.area()}\n And your rectangles perimiter is {rectangle.perimiter()}")

if choice == "2":
    radius = int(input("Please enter the radius of the circle\n"))
    circle = Circle(radius)
    print(f"Your circle area is {circle.area()}\n And your circle perimiter is {circle.perimiter()}")
