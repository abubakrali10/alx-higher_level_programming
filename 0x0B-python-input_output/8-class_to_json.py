#!/usr/bin/python3
""" ``class_to_json`` module
supplies 1 function, class_to_json(obj)
"""


def class_to_json(obj):
    """ dictionary description of an object """
    return obj.__dict__
