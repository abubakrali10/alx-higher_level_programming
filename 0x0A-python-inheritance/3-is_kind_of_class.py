#!/usr/bin/python3
""" ``is_kind_of_class`` module
is_kind_of_class module supplies 1 function, is_kind_of_class(obj, a_class)
"""


def is_kind_of_class(obj, a_class):
    """ checks if obj is instance of a class
    Args:
        obj: first object
        a_class: class to check against
    Return: True if obj is instance of a_class, False otherwise
    """
    return isinstance(obj, a_class)
