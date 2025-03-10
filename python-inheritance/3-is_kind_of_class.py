#!/usr/bin/python3
"""
Defines a function that returns True if the object is an instance of,
or if the object is an instance of a class that inherited from,
the specified class; otherwise False.
"""


def is_kind_of_class(obj, a_class):
    """
    Check if obj is an instance of a_class or any subclass of a_class.

    Args:
        obj: The object to check.
        a_class: The class or superclass to compare with.

    Returns:
        True if isinstance(obj, a_class), False otherwise.
    """
    return isinstance(obj, a_class)
