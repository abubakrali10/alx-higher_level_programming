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

    def area(self):
        """Calculating the area of Rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """Calculating perimeter of Rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """A special method to print the shape of the Rectangle"""
        rectangle_shape = ""
        if self.__width == 0 or self.__height == 0:
            return rectangle_shape
        for i in range(self.__height):
            for j in range(self.__width):
                rectangle_shape += "#"
            if i != self.__height - 1:
                rectangle_shape += "\n"
        return rectangle_shape
