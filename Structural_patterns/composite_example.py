from abc import ABC, abstractmethod

# Composite Design Pattern Explanation:
# The Composite pattern allows you to treat individual objects (leaf nodes) and compositions of objects (composite nodes)
# uniformly. This pattern is especially useful when you have hierarchical structures (like trees).
# In this example, we use the Composite pattern to represent mathematical expressions as a tree structure.
# A number is a leaf, while operations like addition are composites that combine multiple expressions.

class Expression(ABC):
    """
    Component: The base class for all elements in the tree structure.
    Defines the interface for both leaf nodes (Number) and composite nodes (Operation).
    """

    @abstractmethod
    def get_value(self) -> float:
        """
        Calculate the value of the expression.
        This is implemented by both the leaves and the composites.
        """
        raise NotImplementedError()


class Number(Expression):
    """
    Leaf: Represents the terminal node in the tree structure.
    A Number has no children, only a value.
    """

    def __init__(self, value: float):
        self.value = value

    def get_value(self) -> float:
        """
        Return the value of the number.
        """
        return self.value


class Operation(Expression, ABC):
    """
    Composite: Represents non-terminal nodes in the tree structure.
    An Operation has two child expressions (ex1 and ex2) that it operates on.
    """

    def __init__(self, ex1: Expression, ex2: Expression):
        self.ex1 = ex1
        self.ex2 = ex2


class PlusOperation(Operation):
    """
    Concrete Composite: Implements a specific operation (addition).
    Combines the values of its two child expressions.
    """

    def get_value(self) -> float:
        """
        Calculate the result of adding the values of the two child expressions.
        """
        return self.ex1.get_value() + self.ex2.get_value()


# Example usage of the Composite Design Pattern
# Create a tree structure representing the expression (1 + 2) + 3
expression = PlusOperation(PlusOperation(Number(1), Number(2)), Number(3))

# Evaluate the expression and print the result
print(expression.get_value())  # Output: 6
