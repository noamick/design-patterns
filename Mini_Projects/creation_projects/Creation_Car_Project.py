from abc import ABC, abstractmethod

# Abstract Factory Design Pattern
# --------------------------------
# This code demonstrates the Abstract Factory design pattern.
# Abstract Factory is a creational design pattern that provides an interface
# for creating families of related or dependent objects without specifying
# their concrete classes.
#
# Key Components:
# 1. Abstract Products: Define interfaces for a set of products (e.g., Wheel, Car).
# 2. Concrete Products: Implement the interfaces for specific product families
#    (e.g., HyundaiWheel, HyundaiCar).
# 3. Abstract Factory: Declares methods for creating abstract products (e.g., CarFactory).
# 4. Concrete Factory: Implements the creation methods to produce concrete products
#    of a specific family (e.g., HyundaiFactory).
#
# Benefits:
# - Ensures consistency among related objects (e.g., a car always gets a compatible wheel).
# - Isolates client code from concrete implementations, making it easier to swap product families.
#
# Example in this code:
# - `CarFactory` is the Abstract Factory.
# - `HyundaiFactory` is the Concrete Factory.
# - `Wheel` and `Car` are Abstract Products.
# - `HyundaiWheel` and `HyundaiCar` are Concrete Products.
# - The client code (at the bottom) interacts only with the Abstract Factory,
#   ensuring flexibility and extensibility.

class Wheel(ABC):
    @abstractmethod
    def get_wheel_r(self) -> float:
        """
        Returns the radius of the wheel.
        Must be implemented by subclasses.
        """
        raise NotImplementedError()

    def __str__(self) -> str:
        """
        Returns a string representation of the wheel, including its size.
        """
        return f'This is a wheel in size {self.get_wheel_r()}'

class HyundaiWheel(Wheel):
    def get_wheel_r(self) -> float:
        """
        Returns the radius of a Hyundai wheel.
        """
        return 28.0

class Car(ABC):
    def __init__(self):
        # Each car can optionally have a wheel.
        self.wheel: Wheel | None = None

    def set_wheel(self, wheel: Wheel) -> None:
        """
        Associates a wheel with the car.
        """
        self.wheel = wheel

    @abstractmethod
    def get_car_name(self) -> str:
        """
        Returns the name of the car.
        Must be implemented by subclasses.
        """
        raise NotImplementedError()

    def __str__(self) -> str:
        """
        Returns a string representation of the car, including its type and associated wheel.
        """
        return f'Car of type {self.get_car_name()} with a wheel: {self.wheel}'

class HyundaiCar(Car):
    def get_car_name(self) -> str:
        """
        Returns the name of this car type.
        """
        return 'Hyundai'

class CarFactory(ABC):
    @abstractmethod
    def create_wheel(self) -> Wheel:
        """
        Creates and returns a Wheel.
        Must be implemented by subclasses.
        """
        raise NotImplementedError()

    @abstractmethod
    def create_car(self) -> Car:
        """
        Creates and returns a Car.
        Must be implemented by subclasses.
        """
        raise NotImplementedError()

    def create_car_with_wheel(self) -> Car:
        """
        Creates a car, adds a wheel to it, and returns the fully built car.
        """
        car = self.create_car()
        wheel = self.create_wheel()
        car.set_wheel(wheel)
        return car

class HyundaiFactory(CarFactory):
    def create_car(self) -> Car:
        """
        Creates and returns a Hyundai car.
        """
        return HyundaiCar()

    def create_wheel(self) -> Wheel:
        """
        Creates and returns a Hyundai wheel.
        """
        return HyundaiWheel()

# Instantiate a Hyundai factory to create cars and wheels.
factory = HyundaiFactory()

# Create a car without a wheel.
car_without_a_wheel = factory.create_car()

# Create a fully built car with a wheel.
car_with_a_wheel = factory.create_car_with_wheel()

# Print the results to demonstrate the factory's output.
print('car_without_a_wheel:', car_without_a_wheel)
print('car_with_a_wheel:', car_with_a_wheel)



from typing import Self

# The Singleton design pattern ensures that a class has only one instance
# and provides a global point of access to that instance.
# This is useful when we want to manage shared resources or configurations
# where only one instance of a class should exist across the entire application.

class Singleton:
    instance: Self = None  # This is a class variable that will hold the single instance of the class.

    def __init__(self):
        pass  # The constructor is intentionally left empty as we are controlling instance creation via the get_instance method.

    def __str__(self):
        return "This is the Singleton instance."  # When the instance is printed, this message will be shown.

    @classmethod
    def get_instance(cls) -> Self:
        # This method checks if an instance of the class already exists.
        # If it doesn't, it creates a new instance and assigns it to the `instance` variable.
        # This ensures that there is only one instance of Singleton.
        if cls.instance is None:
            cls.instance = cls()  # Create and assign the unique instance.
        return cls.instance  # Return the single instance.

# Global access point to the Singleton class
unique = Singleton.get_instance()  # This is the global access point where we retrieve the unique Singleton instance.

print(unique)  # This prints the unique instance and calls the __str__ method, which outputs: "This is the Singleton instance."



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
    
    
    
    
    
# --------------------------- Explanation of the Factory Pattern ---------------------------

# Factory Design Pattern: This pattern is used to create objects without exposing the instantiation logic to the client.
# It allows for flexible and modular object creation rules.
# In this case, we are using it to create different types of cars (Hyundai, Kaya) through car factories without exposing the creation details to the rest of the code.

# How this is implemented in the code:
# - **Car** is a base class representing a car.
# - **Hyundai** and **Kaya** are different types of cars (creating different objects).
# - **CarFactory** is the factory that creates cars (the `create_car_and_move` method creates a car and moves it to a specific location).
# - **HyundaiFactory** is the specific factory for creating Hyundai cars.

# The use of this pattern allows adding new car types without modifying the rest of the code that manages car creation, making the code more flexible and modular.


from abc import ABC, abstractmethod

class Car(ABC):
    # The constructor of the car initializes its current position.
    def __init__(self):
        self.current_x: int = 0

    # Method to move the car from one position to another.
    # The method takes a target position and updates the current position of the car.
    def move(self, x: int) -> None:
        print(f'the car ({self.get_product_name()}) will move from {self.current_x} to {x}')
        self.current_x = x

    # Abstract method representing the name of the product (the car), must be implemented in every class inheriting from Car.
    @abstractmethod
    def get_product_name(self) -> str:
        raise NotImplementedError()

class Hyundai(Car):
    def get_product_name(self) -> str:
        return 'Hyundai'

class Kaya(Car):
    def get_product_name(self) -> str:
        return 'Kaya'

class CarFactory(ABC):
    # Abstract method to create a car, must be implemented in every class inheriting from CarFactory.
    @abstractmethod
    def create_car(self) -> Car:
        raise NotImplementedError()

    # A general method that creates a car using the create_car method and moves it to position 5.
    def create_car_and_move(self) -> None:
        obj = self.create_car()  # Creating a car
        obj.move(5)  # Moving the car to position 5

class HyundaiFactory(CarFactory):
    def create_car(self) -> Car:
        return Hyundai()  # Returns a new Hyundai object

# Creating an object from the HyundaiFactory
factory = HyundaiFactory()
# Creating a car and moving it to position 5
factory.create_car_and_move()

    # Print the details of both rectangles to demonstrate that rect2 is a copy of rect1.
    print(rect1.__dict__)
    print(rect2.__dict__)
    
    
    
    
    
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
