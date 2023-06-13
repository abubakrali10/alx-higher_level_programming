#!/usr/bin/python3
""" ``from_json_string`` module
supplies 1 function, from_json_string(my_str)
"""
import json


def from_json_string(my_str):
    """ gets object from a string """
    return json.loads(my_str)
