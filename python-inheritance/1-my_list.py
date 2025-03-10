#!/usr/bin/python3
"""
Defines a class MyList that inherits from list.
"""


class MyList(list):
    """
    MyList is a subclass of list with an additional public instance method
    'print_sorted' that prints the list in ascending order.
    """
    def print_sorted(self):
        """
        Prints the list in ascending order without modifying the original list.
        """
        print(sorted(self))
