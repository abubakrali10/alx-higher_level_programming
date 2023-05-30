#!/usr/bin/python3
"""Defining a Square class"""


class Square:
    """Representing Sqaure class"""
    def __init__(self, size=0):
        """initialize square object
        Args:
            size: size of the new created square
        """
        self.__size = size

    @property
    def size(self):
        """get method to retriving size"""
        return self.__size

    @size.setter
    def size(self, value):
        """set method to set size
        Args:
            value: value to set to size
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Returning Square area"""
        return self.__size * self.__size
