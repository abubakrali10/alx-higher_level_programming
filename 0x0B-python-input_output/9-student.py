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

    def to_json(self):
        """ gets a dictionary description of an object"""
        return self.__dict__
