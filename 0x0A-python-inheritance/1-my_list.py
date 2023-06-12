#!/usr/bin/python3
""" ``my_list`` module.
my_list module supplies one function, print_sorted(self)
"""


class MyList(list):
    """ MyList class inherites list"""
    def __init__(self):
        """ Initializing MyList """
        self.__init__ = list()

    def print_sorted(self):
        """ Prints sorted list """
        print(sorted(self))
