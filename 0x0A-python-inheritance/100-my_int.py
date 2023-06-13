#!/usr/bin/python3
""" ``myint`` module
defines a class that inherits from int
"""


class MyInt(int):
    """ MyInt class that inherits from int """
    def __eq__(self, value):
        """ invert == to != """
        return False

    def __ne__(self, value):
        """ invert != to == """
        return True
