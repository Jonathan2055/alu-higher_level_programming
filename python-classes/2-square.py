#!/usr/bin/python3
"""Square that defines a square by: (based on 1-square.py)"""


class Square:
    """Defines a square with size validation."""

    def __init__(self, size=0):
        """Initialize a square with a given size, ensuring validation."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
