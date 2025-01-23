# This code demonstrates the Adapter Design Pattern.
# The Adapter Pattern allows incompatible classes to work together by converting the interface
# of one class into an interface expected by another. In this example, we have:
# 1. `RoundRock` and `RoundHole` represent a circular rock and hole.
# 2. `SquareRock` is incompatible with `RoundHole` because it is based on width and height, not radius.
# 3. `SquareRockAdapter` acts as the adapter by converting a square rock's dimensions into an
#    effective radius, allowing it to be checked against a `RoundHole`.

class RoundRock:
    def __init__(self, radius: float):
        # Initializes a round rock with a given radius.
        self.radius = radius


class RoundHole:
    def __init__(self, radius: float):
        # Initializes a round hole with a given radius.
        self.radius = radius

    def does_rock_fit(self, rock: RoundRock) -> bool:
        # Checks if the rock's radius is smaller than the hole's radius.
        return rock.radius < self.radius


class SquareRock:
    def __init__(self, width: float, height: float):
        # Initializes a square rock with a given width and height.
        self.width = width
        self.height = height


class SquareRockAdapter(RoundRock):
    def __init__(self, square_rock: SquareRock):
        # Converts the square rock into a compatible round rock by calculating the effective radius
        # (diagonal length divided by 2).
        radius = (square_rock.height**2 + square_rock.width**2)**0.5
        super().__init__(radius)
        self.square_rock = square_rock


if __name__ == '__main__':
    # Create a round rock with a radius of 10 and a round hole with a radius of 11.
    round_rock = RoundRock(10)
    round_hole = RoundHole(11)
    # Check if the round rock fits into the round hole.
    print('Does the rock fit the hole?', round_hole.does_rock_fit(round_rock))

    # Create a square rock with width 3 and height 4.
    square_rock = SquareRock(3, 4)
    # Use the adapter to calculate its effective radius and check if it fits into the round hole.
    print('Does the square rock fit the hole?', round_hole.does_rock_fit(SquareRockAdapter(square_rock)))

