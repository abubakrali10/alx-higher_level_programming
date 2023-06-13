#!/usr/bin/python3
""" ``rectangle`` module
rectangle module inherit from BaseGeometry
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

    def area(self):
        "Calculate rectangle area"
        return self.__width * self.__height

    def __str__(self):
        """ method to print class as a string"""
        return f"[Rectangle] {self.__width}/{self.__height}"
