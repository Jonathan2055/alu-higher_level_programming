#!/usr/bin/python3
"""
Defines a function that returns True if the object is an instance of a class
that inherited (directly or indirectly) from the specified class; otherwise
False.
"""


def inherits_from(obj, a_class):
    """
    Check if the object's class inherited from a_class.

    Args:
        obj: The object to check.
        a_class: The class that might be a parent of type(obj).

    Returns:
        bool: True if type(obj) is not a_class and type(obj) is a subclass of
        a_class, otherwise False.
    """
    return type(obj) is not a_class and issubclass(type(obj), a_class)
