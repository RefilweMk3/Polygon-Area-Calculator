from abc import ABC, abstractmethod
import math

class Polygon(ABC):
    @abstractmethod
    def area(self):
        pass

class Triangle(Polygon):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def area(self):
        return 0.5 * self.base * self.height

class Rectangle(Polygon):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

class Pentagon(Polygon):
    def __init__(self, side, angle):
        self.side = side
        self.angle = angle
    def area(self):
        perimeter = 5 * self.side
        return 0.5 * perimeter * self.angle
    
class Hexagon(Polygon):
    def __init__(self, side):
        self.side = side

    def area(self):
        return (3 * math.sqrt(3) / 2) * self.side ** 2

triangle = Triangle(10, 5)
print(f"Triangle area: {triangle.area()}")

rectangle = Rectangle(10, 5)
print(f"Rectangle area: {rectangle.area()}")

square = Square(4)
print(f"Square area: {square.area()}")

pentagon = Pentagon(6, 4)
print(f"Pentagon area: {pentagon.area()}")

hexagon = Hexagon(6)
print(f"Hexagon area: {hexagon.area()}")
