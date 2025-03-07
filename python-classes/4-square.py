#!/usr/bin/python3
"""a class Square that defines a square by: (based on 3-square.py)"""


class Square:
    """Defines a square with size validation, area computation, and property access."""

    def __init__(self, size=0):
        """Initialize a square with a given size, ensuring validation."""
        self.size = size  # Using the property setter for validation

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the current square area."""
        return self.__size ** 2
