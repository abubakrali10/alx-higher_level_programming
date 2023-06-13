#!/usr/bin/python3
import json
""" ``to_json_string`` module
supplies 1 function, to_json_string(my_obj)
"""


def to_json_string(my_obj):
    """ gets the JSON representation of an object """
    return json.dumps(my_obj)
