#!/usr/bin/python3
"""
''Square'' module
creating a Square that inherits a Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Representing a Square class """
    def __init__(self, size, x=0, y=0, id=None):
        """ Initializing a square """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ Retriving a square size """
        return self.width

    @size.setter
    def size(self, val):
        """ Setting the square size """
        self.width = val
        self.height = val

    def update(self, *args, **kwargs):
        """ updating square attriubutes """
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
        """ Returns the dicitionary representation of Square """
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }

    def __str__(self):
        """ Returns the string representation of Square """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
