#!/usr/bin/python3
"""
Defines a function that returns True if the object is exactly an instance
of the specified class, otherwise False.
"""


def is_same_class(obj, a_class):
    """
    Check if the object is exactly an instance of a_class.

    Args:
        obj: The object to check.
        a_class: The class to compare with.

    Returns:
        True if type(obj) is exactly a_class, False otherwise.
    """
    return type(obj) is a_class
