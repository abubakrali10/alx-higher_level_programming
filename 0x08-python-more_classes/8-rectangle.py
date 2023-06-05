#!/usr/bin/python3
"""
Defines a Rectangle class include attributes and methods
"""


class Rectangle:
    """Representing the Rectangle class"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """initalizing the Rectangle
        Args:
            width: width of the Rectangle
            height: height of the Rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
                rectangle_shape += str(self.print_symbol)
            if i != self.__height - 1:
                rectangle_shape += "\n"
        return rectangle_shape

    def __repr__(self):
        """String representation of creating Rectangle instance"""
        rec_instance = "Rectangle(" + str(self.__width)
        rec_instance += ", " + str(self.__height) + ")"
        return rec_instance

    def __del__(self):
        """Printing a message when instance is destroyed"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Checking the biggest Rectangle
        Args:
            rect_1: first Rectangle instance
            rect_2: second Rectangle instance
        Raises:
            TypeError: if one or both Args in not Rectangle instance
        Return:
            The biggest instance of Rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
