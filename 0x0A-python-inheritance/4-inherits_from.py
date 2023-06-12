#!/usr/bin/python3
""" ``inherits_from`` module
inherits_from module supplies 1 function, inherits_from(obj, a_class)
"""


def inherits_from(obj, a_class):
    """ checks if object is an instance of a class
    That inherited from a specific class
    Args:
        obj: object
        a_class: class to check against
    Return: True if object is an instance of a class, False otherwise
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
