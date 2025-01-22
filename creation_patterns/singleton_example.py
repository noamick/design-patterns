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
