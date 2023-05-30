#!/usr/bin/python3
"""Defining a Square class"""


class Square:
    """Representing an empty Sqaure class"""
    def __init__(self, size=0):
        """initialize square object
        Args:
            size: size of the new created square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
