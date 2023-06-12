#!/usr/bin/python3
""" ``is_same_class`` module
is_same_module supplies 1 function, is_same_class(obj, a_class)
"""


def is_same_class(obj, a_class):
    """ checks for same class
    Args:
        obj: first object
        a_class: class to check against
    Return: True is same class, False otherwise
    """
    return type(obj) == a_class
