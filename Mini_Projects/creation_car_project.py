from typing import Self
from abc import ABC, abstractmethod

#abstract_factory

class Wheel(ABC):

    @abstractmethod
    def get_wheel_r(self) -> float:
        raise NotImplementedError()

    def __str__(self) -> str:
        return f'this is a wheel in size {self.get_wheel_r()}'


class HyundaiWheel(Wheel):
    def get_wheel_r(self) -> float:
        return 28.0


class Car(ABC):

    def __init__(self):
        self.wheel: Wheel | None = None

    def set_wheel(self, wheel: Wheel) -> None:
        self.wheel = wheel

    @abstractmethod
    def get_car_name(self) -> str:
        raise NotImplementedError()

    def __str__(self) -> str:
        return f'Car of type {self.get_car_name()} with a wheel: {self.wheel}'


class HyundaiCar(Car):
    def get_car_name(self) -> str:
        return 'Hyundai'


class CarFactory(ABC):
    @abstractmethod
    def create_wheel(self) -> Wheel:
        raise NotImplementedError()

    @abstractmethod
    def create_car(self) -> Car:
        raise NotImplementedError()

    def create_car_with_wheel(self) -> Car:
        car = self.create_car()
        wheel = self.create_wheel()
        car.set_wheel(wheel)
        return car


class HyundaiFactory(CarFactory):
    def create_car(self) -> Car:
        return HyundaiCar()

    def create_wheel(self) -> Wheel:
        return HyundaiWheel()



#factory_method

class Car(ABC):
    def __init__(self):
        self.current_x: int = 0

    def move(self, x: int) -> None:
        print(f'the car ({self.get_product_name()}) will move from {self.current_x} to {x}')
        self.current_x = x

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
    @abstractmethod
    def create_car(self) -> Car:
        raise NotImplementedError()

    def create_car_and_move(self) -> None:
        obj = self.create_car()
        obj.move(5)


class HuyndaiFactory(CarFactory):

    def create_car(self) -> Car:
        return Hyundai()



#builder

class Home:

    def __init__(self):
        self.roof: bool = False
        self.garden: bool = True
        self.rooms: int = 0


class HomeBuilder:

    def __init__(self, home: Home):
        self.home = home

    def build_roof(self) -> None:
        self.home.roof = True

    def build_room(self) -> None:
        self.home.rooms += 1


class ApartmentDirector:
    @classmethod
    def create_home(cls) -> Home:
        home = Home()
        builder = HomeBuilder(home)

        for i in range(3):
            builder.build_room()
        builder.build_roof()
        return home



#prototype
class Shape(ABC):

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    @abstractmethod
    def clone(self) -> Self:
        raise NotImplementedError()


class Circle(Shape):

    def __init__(self, radius: float, x: float, y: float):
        super().__init__(x, y)
        self.radius = radius

    def clone(self) -> Self:
        return Circle(self.radius, self.x, self.y)


class Rectangle(Shape):

    def __init__(self, height: float, width: float, x: float, y: float):
        super().__init__(x, y)
        self.height = height
        self.width = width

    def clone(self) -> Self:
        return Rectangle(self.height, self.width, self.x, self.y)


# singleton

class Singleton:
    instance: Self = None

    def __init__(self):
        pass

    @classmethod
    def get_instance(cls) -> Self:
        if cls.instance is None:
            cls.instance = cls()
        return cls.instance



if __name__ == '__main__':
    # Singleton: VehicleFactoryManager instance to manage factories
    class VehicleFactoryManager(Singleton):
        def __init__(self):
            if not hasattr(self, "factories"):
                self.factories = []

        def register_factory(self, factory: CarFactory):
            self.factories.append(factory)

        def list_factories(self):
            return self.factories

    factory_manager = VehicleFactoryManager.get_instance()

    # Abstract Factory: Create cars and wheels
    hyundai_factory = HyundaiFactory()
    factory_manager.register_factory(hyundai_factory)

    # Create a car with and without wheels using Abstract Factory
    print("Abstract Factory Example:")
    car_with_wheel = hyundai_factory.create_car_with_wheel()
    print(f"Car with wheel: {car_with_wheel}")

    car_without_wheel = hyundai_factory.create_car()
    print(f"Car without wheel: {car_without_wheel}")

    # Factory Method: Create and move a Hyundai car
    print("\nFactory Method Example:")
    hyundai_car_factory = HuyndaiFactory()
    hyundai_car_factory.create_car_and_move()

    # Builder: Construct a car showroom with homes (simulation)
    print("\nBuilder Example:")
    apartment = ApartmentDirector.create_home()
    print(f"Home constructed: {apartment.roof}, rooms: {apartment.rooms}, garden: {apartment.garden}")

    # Prototype: Clone a car design
    print("\nPrototype Example:")
    prototype_rectangle = Rectangle(3, 4, 10, 20)
    cloned_rectangle = prototype_rectangle.clone()
    print(f"Original Rectangle: {vars(prototype_rectangle)}")
    print(f"Cloned Rectangle: {vars(cloned_rectangle)}")

    # Singleton: Verify factory manager instance is the same
    print("\nSingleton Example:")
    another_factory_manager = VehicleFactoryManager.get_instance()
    print(f"Are both factory manager instances the same? {factory_manager is another_factory_manager}")
