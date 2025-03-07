#!/usr/bin/python3
""" a class Square that defines a square by: (based on 2-square.py)"""


class Square:
    """Defines a square with size validation and area computation."""

    def __init__(self, size=0):
        """Initialize a square with a given size, ensuring validation."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns the current square area."""
        return self.__size ** 2
