from abc import ABC, abstractmethod
from typing import Self

# The Prototype design pattern allows creating new objects by cloning existing ones
# instead of creating them from scratch. This pattern is particularly useful when
# object creation is resource-intensive or when the object structure is complex.
# Key concepts:
# 1. Define a clone interface in a base class or interface.
# 2. Concrete classes implement the clone method to return a copy of themselves.
# 3. This approach reduces dependencies on constructors and makes object creation more flexible.

class Shape(ABC):
    """
    Abstract base class representing a generic shape.
    It enforces the implementation of the clone method in derived classes.
    """

    def __init__(self, x: float, y: float):
        """
        Initialize the shape with x and y coordinates.
        """
        self.x = x
        self.y = y

    @abstractmethod
    def clone(self) -> Self:
        """
        Abstract method for cloning the object.
        Must be implemented by all subclasses.
        """
        raise NotImplementedError()


class Circle(Shape):
    """
    Concrete implementation of a Shape that represents a Circle.
    Includes an additional property for the radius of the circle.
    """

    def __init__(self, radius: float, x: float, y: float):
        """
        Initialize the circle with a radius and coordinates (x, y).
        """
        super().__init__(x, y)
        self.radius = radius

    def clone(self) -> Self:
        """
        Create and return a copy of the current Circle instance.
        """
        return Circle(self.radius, self.x, self.y)


class Rectangle(Shape):
    """
    Concrete implementation of a Shape that represents a Rectangle.
    Includes additional properties for height and width.
    """

    def __init__(self, height: float, width: float, x: float, y: float):
        """
        Initialize the rectangle with height, width, and coordinates (x, y).
        """
        super().__init__(x, y)
        self.height = height
        self.width = width

    def clone(self) -> Self:
        """
        Create and return a copy of the current Rectangle instance.
        """
        return Rectangle(self.height, self.width, self.x, self.y)


if __name__ == '__main__':
    # Create an instance of a Rectangle with specific dimensions and position.
    rect1 = Rectangle(2, 2, 2, 2)

    # Clone the Rectangle to create a new instance with identical properties.
    rect2 = rect1.clone()

    # Print the details of both rectangles to demonstrate that rect2 is a copy of rect1.
    print(rect1.__dict__)
    print(rect2.__dict__)
