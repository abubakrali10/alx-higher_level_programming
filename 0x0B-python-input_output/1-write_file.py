#!/usr/bin/python3
""" ``write_file`` module
supplies 1 function, writefile(filename="", text="")
"""


def write_file(filename="", text=""):
    """writes a text into a file"""
    with open(filename, 'w', encoding='utf-8') as f:
        the_txt = f.write(text)
        return the_txt
