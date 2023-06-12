#!/usr/bin/python3
""" ``base_geometry`` module
base_geometry module supplies 1 function, area()
"""


class BaseGeometry:
    """BaseGeometry class represents the base geometry shape"""
    def area(self):
        """ Raises Exception """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ method to validate value as integer """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
