#!/usr/bin/python3
"""
Defines a class BaseGeometry with an unimplemented area method.
"""


class BaseGeometry:
    """
    A class representing base geometry.
    """

    def area(self):
        """
        Raises an exception indicating that the method is not implemented.
        """
        raise Exception("area() is not implemented")
