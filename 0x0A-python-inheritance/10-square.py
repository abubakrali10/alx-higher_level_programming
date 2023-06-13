#!/usr/bin/python3
""" ``square`` module
square module inherits from Rectangle
"""


rectangle = __import__('9-rectangle').Rectangle


class Square(rectangle):
    """ Square class that inherits Rectangle """
    def __init__(self, size):
        """ Initializing Square
        Args:
            size: size of square
        """
        super().integer_validator('size', size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        "Calculate Square area"
        return self.__size ** 2
