#!/usr/bin/python3
"""
Defines a Rectangle class include attributes and methods
"""


class Rectangle:
    """Representing the Rectangle class"""

    def __init__(self, width=0, height=0):
        """initalizing the Rectangle
        Args:
            width: width of the Rectangle
            height: height of the Rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retriving the width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setting the width attribute
        Args:
            value: value to set width
        Raises:
            TypeError: if value is not integer
            ValueError: if value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retriving the height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setting the height attribute
        Args:
            value: value to set height
        Raises:
            TypeError: if value is not integer
            ValueError: if value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
