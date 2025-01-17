# The Builder design pattern separates the construction of a complex object from its representation.
# This pattern is particularly useful when an object requires many steps to be fully constructed,
# and the construction process can vary depending on the use case.

class Home:
    # Represents the final product to be built.
    def __init__(self):
        self.roof: bool = False  # Indicates if the home has a roof.
        self.garden: bool = True  # Indicates if the home includes a garden (default is True).
        self.rooms: int = 0  # The number of rooms in the home.

    def __str__(self) -> str:
        # String representation of the home's attributes.
        print("roof: ", self.roof)
        print("rooms ", self.rooms)
        return ""


class HomeBuilder:
    # Builder class responsible for constructing parts of the 'Home' object.
    def __init__(self, home: Home):
        self.home = home  # Holds the instance of Home being constructed.

    def build_roof(self) -> None:
        # Adds a roof to the home.
        self.home.roof = True

    def build_room(self) -> None:
        # Adds a single room to the home.
        self.home.rooms += 1


class ApartmentDirector:
    # Director class that oversees the construction process using the builder.
    @classmethod
    def create_home(cls) -> Home:
        # Directs the step-by-step construction of a Home.
        home = Home()  # Creates the Home instance to be built.
        builder = HomeBuilder(home)  # Assigns a builder to manage construction.

        # Constructs the home by adding 3 rooms and a roof.
        for i in range(3):
            builder.build_room()
        builder.build_roof()
        return home  # Returns the fully constructed Home object.


# Usage example:
home = ApartmentDirector.create_home()
print(home)
