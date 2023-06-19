#!/usr/bin/python3
"""
''Rectangle'' module
Creating a Rectangle class that inherits Base
"""
import json
from models.base import Base


class Rectangle(Base):
    """ a class that describing a rectangle
    and inherits from a Base class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ initializing a Rectangle instance
        Args:
            width: the width of rectangle
            height: the height of rectangle
            x: x position of rectangle
            y: y position of rectangle
            id: unique id for every instance
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """
        retriving method for the Rectangle width
        """
        return self.__width

    @width.setter
    def width(self, val):
        """
        setting and validating the width attribute
        Args:
            val: value to set to width after validating
        """
        if type(val) is not int:
            raise TypeError("width must be an integer")
        if val <= 0:
            raise ValueError("width must be >= 0")
        self.__width = val

    @property
    def height(self):
        """
        Retriving method for the rectangle height
        """
        return self.__height

    @height.setter
    def height(self, val):
        """
        Setting and validating the height attribute
        Args:
            val: value to set to height after validating
        """
        if type(val) is not int:
            raise TypeError("height must be an integer")
        if val <= 0:
            raise ValueError("height must be >= 0")
        self.__height = val

    @property
    def x(self):
        """
        Retriving method for rectangle x attribute
        """
        return self.__x

    @x.setter
    def x(self, val):
        """
        Setting and validating a rectangle x attribute
        Args:
            val: value to set to x attriubte after validating
        """
        if type(val) is not int:
            raise TypeError("x must be an integer")
        if val < 0:
            raise ValueError("x must be >= 0")
        self.__x = val

    @property
    def y(self):
        """
        retriving method for rectangle y attribute
        """
        return self.__y

    @y.setter
    def y(self, val):
        """
        Setting and validating a rectangle y attribute
        Args:
            val: value to set to y after validating
        """
        if type(val) is not int:
            raise TypeError("y must be an integer")
        if val < 0:
            raise ValueError("y must be >= 0")
        self.__y = val

    def area(self):
        """
        Calculating the rectangle area
        Retruns the width multiplied by height
        """
        return self.width * self.height

    def display(self):
        """
        printing the rectangle shape using #
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
        updating the rectangle attributes
        by assigning an argument to each attribute
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
        Returns the dicitionary representation of The Rectangle
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
        Returns the string representation of The Rectangle
        """
        return f"[Rectangle] ({self.id})" +
        "{self.x}/{self.y} - {self.width}/{self.height}"
