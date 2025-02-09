from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Self

# Decorator Design Pattern:
# This pattern is used to dynamically extend the functionality of objects without modifying their structure.
# It allows behavior to be added to individual objects, either statically or dynamically.
# In this implementation, we use decorators to modify color values by incrementing specific RGB components.

class Color:
    # Represents a color with RGB values.
    def __init__(self, r: int, g: int, b: int):
        self.r = r
        self.g = g
        self.b = b

    def copy(self) -> Self:
        # Returns a copy of the current color object.
        return Color(self.r, self.g, self.b)

    def __str__(self) -> str:
        return f"({self.r} , {self.g} , {self.b})"

class ColorOperator(ABC):
    # Abstract base class for color modification operations.
    def __init__(self, next_operator: ColorOperator = None):
        self.next_operator = next_operator

    @abstractmethod
    def operate(self, color: Color) -> Color:
        # Abstract method to be implemented by subclasses to modify the color.
        raise NotImplementedError()

class MakeReder(ColorOperator):
    # Concrete decorator that increases the red component of a color.
    def operate(self, color: Color) -> Color:
        color_1 = color.copy()
        color_1.r += 1
        if self.next_operator:
            color_1 = self.next_operator.operate(color_1)
        return color_1

class MakeGreener(ColorOperator):
    # Concrete decorator that increases the green component of a color.
    def operate(self, color: Color) -> Color:
        color_1 = color.copy()
        color_1.g += 1
        if self.next_operator:
            color_1 = self.next_operator.operate(color_1)
        return color_1

# How this code implements the Decorator Pattern:
# - `ColorOperator` acts as the base decorator class, defining a common interface.
# - `MakeReder` and `MakeGreener` are concrete decorators that modify a color.
# - Each decorator can wrap another decorator (`next_operator`), allowing multiple modifications to be chained dynamically.
# - This enables us to modify an object's behavior (color transformation) without altering the original `Color` class.

if __name__ == '__main__':
    color = Color(1, 1, 1)  # Initial color (1,1,1)
    oper_1 = MakeGreener(MakeReder(MakeReder()))  # Apply two red increments and one green increment
    color_2 = oper_1.operate(color)  # Perform the chained modifications
    print(color_2)  # Output: (3, 2, 1)