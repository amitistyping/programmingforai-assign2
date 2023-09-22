import math

#parent shape class
class Shape:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def getArea(self):
        pass  # will be implmented by child classes

# circle child class
class Circle(Shape):
    def __init__(self, name, color, radius):
        super().__init__(name, color)
        self.radius = radius

    def getArea(self):
        return math.pi * self.radius**2

    def getPerimeter(self):
        return 2 * math.pi * self.radius

# square child class
class Square(Shape):
    def __init__(self, name, color, side_length):
        super().__init__(name, color)
        self.side_length = side_length

    def getArea(self):
        return self.side_length**2

# triangle child class
class Triangle(Shape):
    def __init__(self, name, color, base, height):
        super().__init__(name, color)
        self.base = base
        self.height = height

    def getArea(self):
        return 0.5 * self.base * self.height


circle = Circle("Circle", "Red", 5)
square = Square("Square", "Blue", 4)
triangle = Triangle("Triangle", "Green", 3, 6)

# calling getArea for each of child class objects
print(f"{circle.name} (Color: {circle.color}) Area: {circle.getArea()}")
print(f"{square.name} (Color: {square.color}) Area: {square.getArea()}")
print(f"{triangle.name} (Color: {triangle.color}) Area: {triangle.getArea()}")
