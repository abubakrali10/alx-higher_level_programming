#!/usr/bin/python3
""" Defines a function to read file """


def read_file(filename=""):
    """ prints a txt file to stdout """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
