#!/usr/bin/python3
""" ``lookup`` module.
lookup module supplies one function, lookup(obj)
"""


def lookup(obj):
    """ function to get attributes and methods in obj
    Args:
        obj: object
    """
    return dir(obj)
