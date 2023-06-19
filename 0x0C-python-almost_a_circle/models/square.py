#!/usr/bin/python3
"""
This module defines the Square class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class represents a square shape.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a Square instance.

        Args:
            size (int): The size of the square.
            x (int): The x-coordinate of the square's position.
            y (int): The y-coordinate of the square's position.
            id (int): The ID of the square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Getter for the size property.

        Returns:
            int: The size of the square.
        """
        return self.width

    @size.setter
    def size(self, val):
        """
        Setter for the size property.

        Args:
            val (int): The size value to set.

        Raises:
            TypeError: If val is not an integer.
            ValueError: If val is less than or equal to 0.
        """
        self.width = val
        self.height = val

    def update(self, *args, **kwargs):
        """
        Updates the attributes of the square.

        Args:
            *args: Variable length argument list.
                - If provided, the arguments are treated as:
                    arg1: The ID of the square.
                    arg2: The size of the square.
                    arg3: The x-coordinate of the square's position.
                    arg4: The y-coordinate of the square's position.
            **kwargs: Keyword arguments.
                - If provided, the arguments are treated as:
                    key='id': The ID of the square.
                    key='size': The size of the square.
                    key='x': The x-coordinate of the square's position.
                    key='y': The y-coordinate of the square's position.
        """
        if len(args) > 0:
            i = 0
            for arg in args:
                if i == 0:
                    self.id = arg
                if i == 1:
                    self.width = arg
                    self.height = arg
                if i == 2:
                    self.x = arg
                if i == 3:
                    self.y = arg
                i = i + 1
        elif len(kwargs) > 0:
            for key, val in kwargs.items():
                if key == 'id':
                    self.id = val
                if key == 'size':
                    self.width = val
                    self.height = val
                if key == 'x':
                    self.x = val
                if key == 'y':
                    self.y = val

    def to_dictionary(self):
        """
        Converts the square to a dictionary representation.

        Returns:
            dict: A dictionary containing the attributes of the square.
        """
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }

    def __str__(self):
        """
        Returns a string representation of the square.

        Returns:
            str: A string representing the square.
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
