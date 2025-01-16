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