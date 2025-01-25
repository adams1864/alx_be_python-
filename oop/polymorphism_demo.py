import math

class Shape:
    def area(self):
        """Base method to be overridden by subclasses."""
        raise NotImplementedError("Subclasses must implement the area method")

class Rectangle(Shape):
    def __init__(self, length, width):
        """Constructor method for initializing the rectangle's dimensions."""
        self.length = length
        self.width = width

    def area(self):
        """Override method to calculate the area of the rectangle."""
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        """Constructor method for initializing the circle's radius."""
        self.radius = radius

    def area(self):
        """Override method to calculate the area of the circle."""
        return math.pi * (self.radius ** 2)
