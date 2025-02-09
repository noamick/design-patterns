from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Self


class Color:

    def __init__(self, r: int, g: int, b: int):
        self.r = r
        self.g = g
        self.b = b

    def copy(self) -> Self:
        return Color(self.r, self.g, self.b)

    def __str__(self) -> str:
        return f"({self.r} , {self.g} , {self.b})"


class ColorOperator(ABC):

    def __init__(self, next_operator: ColorOperator = None):
        self.next_operator = next_operator

    @abstractmethod
    def operate(self, color: Color) -> Color:
        raise NotImplementedError()


class MakeReder(ColorOperator):

    def operate(self, color: Color) -> Color:
        color_1 = color.copy()
        color_1.r += 1
        if self.next_operator:
            color_1 = self.next_operator.operate(color_1)
        return color_1


class MakeGreener(ColorOperator):

    def operate(self, color: Color) -> Color:
        color_1 = color.copy()
        color_1.g += 1
        if self.next_operator:
            color_1 = self.next_operator.operate(color_1)
        return color_1


if __name__ == '__main__':
    color = Color(1, 1, 1)
    oper_1 = MakeGreener(MakeReder(MakeReder()))
    color_2 = oper_1.operate(color)
    print(color_2)

