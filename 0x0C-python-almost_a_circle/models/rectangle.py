#!/usr/bin/python3
"""
This module defines the Rectangle class.
"""

from models.base import Base


class Rectangle(Base):
    """
    Rectangle class represents a rectangle shape.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int): The x-coordinate of the rectangle's position.
            y (int): The y-coordinate of the rectangle's position.
            id (int): The ID of the rectangle.

        Raises:
            TypeError: If width, height, x, or y is not an integer.
            ValueError: If width, height, x, or y is less than or equal to 0.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """
        Getter for the width property.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, val):
        """
        Setter for the width property.

        Args:
            val (int): The width value to set.

        Raises:
            TypeError: If val is not an integer.
            ValueError: If val is less than or equal to 0.
        """
        if type(val) is not int:
            raise TypeError("width must be an integer")
        if val <= 0:
            raise ValueError("width must be >= 0")
        self.__width = val

    @property
    def height(self):
        """
        Getter for the height property.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, val):
        """
        Setter for the height property.

        Args:
            val (int): The height value to set.

        Raises:
            TypeError: If val is not an integer.
            ValueError: If val is less than or equal to 0.
        """
        if type(val) is not int:
            raise TypeError("height must be an integer")
        if val <= 0:
            raise ValueError("height must be >= 0")
        self.__height = val

    @property
    def x(self):
        """
        Getter for the x property.

        Returns:
            int: The x-coordinate of the rectangle's position.
        """
        return self.__x

    @x.setter
    def x(self, val):
        """
        Setter for the x property.

        Args:
            val (int): The x-coordinate value to set.

        Raises:
            TypeError: If val is not an integer.
            ValueError: If val is less than 0.
        """
        if type(val) is not int:
            raise TypeError("x must be an integer")
        if val < 0:
            raise ValueError("x must be >= 0")
        self.__x = val

    @property
    def y(self):
        """
        Getter for the y property.

        Returns:
            int: The y-coordinate of the rectangle's position.
        """
        return self.__y

    @y.setter
    def y(self, val):
        """
        Setter for the y property.

        Args:
            val (int): The y-coordinate value to set.

        Raises:
            TypeError: If val is not an integer.
            ValueError: If val is less than 0.
        """
        if type(val) is not int:
            raise TypeError("y must be an integer")
        if val < 0:
            raise ValueError("y must be >= 0")
        self.__y = val

    def area(self):
        """
        Calculates the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.width * self.height

    def display(self):
        """
        Displays the rectangle by printing it using '#' characters.
        """
        for _ in range(self.y):
            print("")
        for _ in range(self.height):
            for _ in range(self.x):
                print(" ", end="")
            for _ in range(self.width):
                print("#", end="")
            print("")

    def update(self, *args, **kwargs):
        """
        Updates the attributes of the rectangle.

        Args:
            *args: Variable length argument list.
                - If provided, the arguments are treated as:
                    arg1: The ID of the rectangle.
                    arg2: The width of the rectangle.
                    arg3: The height of the rectangle.
                    arg4: The x-coordinate of the rectangle's position.
                    arg5: The y-coordinate of the rectangle's position.
            **kwargs: Keyword arguments.
                - If provided, the arguments are treated as:
                    key='id': The ID of the rectangle.
                    key='width': The width of the rectangle.
                    key='height': The height of the rectangle.
                    key='x': The x-coordinate of the rectangle's position.
                    key='y': The y-coordinate of the rectangle's position.
        """
        if len(args) > 0:
            i = 0
            for arg in args:
                if i == 0:
                    self.id = arg
                if i == 1:
                    self.width = arg
                if i == 2:
                    self.height = arg
                if i == 3:
                    self.x = arg
                if i == 4:
                    self.y = arg
                i = i + 1
        elif len(kwargs) > 0:
            for key, val in kwargs.items():
                if key == 'id':
                    self.id = val
                if key == 'width':
                    self.width = val
                if key == 'height':
                    self.height = val
                if key == 'x':
                    self.x = val
                if key == 'y':
                    self.y = val

    def to_dictionary(self):
        """
        Converts the rectangle to a dictionary representation.

        Returns:
            dict: A dictionary containing the attributes of the rectangle.
        """
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }

    def __str__(self):
        """
        Returns a string representation of the rectangle.

        Returns:
            str: A string representing the rectangle.
        """
        return f"[Rectangle] ({self.id}) {self.x}/{self.y}" +
        "- {self.width}/{self.height}"
