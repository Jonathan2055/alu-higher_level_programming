#!/usr/bin/python3
"""
This module provides a function that returns the list of available attributes
and methods of any given object in Python. It adheres to the assignment
requirements by not importing any external modules.
"""


def lookup(obj):
    """Return the list of available attributes and methods of an object."""
    return dir(obj)
