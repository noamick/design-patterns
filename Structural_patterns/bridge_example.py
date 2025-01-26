# Bridge Design Pattern
# The Bridge pattern is a structural design pattern that decouples an abstraction (in this case, Shape)
# from its implementation (in this case, Color) so that the two can be developed independently.
# This pattern is useful when you need to cross two orthogonal dimensions of variability (e.g., different shapes and different colors).

from abc import ABC, abstractmethod

# Implementor: Defines the interface for the implementation (color in this case).
class Color(ABC):

    @abstractmethod
    def get_ansi_code(self) -> str:
        # Provides the ANSI code for the color (used for terminal text coloring).
        raise NotImplementedError()

    @abstractmethod
    def get_name(self) -> str:
        # Provides the name of the color.
        raise NotImplementedError()

    def get_color_text(self, text: str) -> str:
        # Returns the text wrapped in the appropriate color code for the terminal.
        return f"\033[{self.get_ansi_code()}{text}\033[0m"

# Concrete Implementor: Implements the Color interface for red.
class ColorRed(Color):

    def get_name(self) -> str:
        return 'red'

    def get_ansi_code(self) -> str:
        return "31m"

# Concrete Implementor: Implements the Color interface for blue.
class ColorBlue(Color):
    def get_name(self) -> str:
        return 'blue'

    def get_ansi_code(self) -> str:
        return "34m"

# Abstraction: Defines the interface for shapes and maintains a reference to a Color object.
class Shape(ABC):

    def __init__(self, color: Color):
        self.color = color  # Bridge: The shape delegates color-related responsibilities to the Color object.

    @abstractmethod
    def print(self) -> None:
        # Abstract method to print details of the shape.
        raise NotImplementedError()

# Refined Abstraction: Implements the Shape interface for a Circle.
class Circle(Shape):
    def print(self) -> None:
        # Prints the shape's details, using the Color object for color-specific logic.
        print(self.color.get_color_text(f'This is a Circle with color {self.color.get_name()}'))

# Example usage of the Bridge pattern.
if __name__ == '__main__':
    # Create a Circle with the red color and print its details.
    Circle(ColorRed()).print()

    # Create a Circle with the blue color and print its details.
    Circle(ColorBlue()).print()
