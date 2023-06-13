#!/usr/bin/python3
""" ``student`` module
supplies 1 function, def to_json(self)
"""


class Student:
    """ a class that defines a student """
    def __init__(self, first_name, last_name, age):
        """ Initializing student """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ get a dictionary description of an object """
        my_dict = {}
        if type(attrs) is list:
            for i in attrs:
                if type(i) is not str:
                    return self.__dict__
            for key, value in self.__dict__.items():
                if key in attrs:
                    my_dict[key] = value
            return my_dict
        return self.__dict__
