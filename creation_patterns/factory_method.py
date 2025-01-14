
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
