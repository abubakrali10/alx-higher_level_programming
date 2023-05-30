#!/usr/bin/python3
"""Defining a Square class"""


class Square:
    """Representing Sqaure class"""
    def __init__(self, size=0, position=(0, 0)):
        """initialize square object
        Args:
            size: size of the new created square
            position: position of the new created square
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """get method to retrive size"""
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

    @property
    def position(self):
        """get method to retrive position"""
        return self.__position

    @position.setter
    def position(self, value):
        """setter method to set position
        Args:
            value: value to set to position
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(i, int) for i in value) or
                not all(i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returning Square area"""
        return self.__size * self.__size

    def my_print(self):
        """printing the square"""
        if self.__size <= 0:
            print("")
            return
        for i in range(self.__position[1]):
            print("")
        for i in range(self.__size):
            print(" " * self.__position[0], end="")
            print("#" * self.__size)
