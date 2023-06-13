#!/usr/bin/python3
" Adds an attribute to an object"


def add_attribute(object, att, value):
    """ Adds a new attribute to an object """

    if hasattr(object, "__dict__") is False:
        raise TypeError("can't add new attribute")
    setattr(object, att, value)
