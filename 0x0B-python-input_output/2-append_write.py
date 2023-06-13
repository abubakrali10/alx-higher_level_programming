#!/usr/bin/python3
""" ``append_write`` module
supplies 1 function, append_write(filename="", text="")
"""


def append_write(filename="", text=""):
    """append a text into the end of a file"""
    with open(filename, 'a', encoding='utf-8') as f:
        char_num = f.write(text)
        return char_num
