#!/usr/bin/python3
""" ``rectangle`` module
rectangle module inherite from BaseGeometry
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle class that inherited BaseGeometry """
    def __init__(self, width, height):
        """ Initializing Rectangle
        Args:
            width: Rectangle width
            height: Rectangle height
        """
        self.__width = width
        self.__height = height
        super().integer_validator('width', width)
        super().integer_validator('height', height)
