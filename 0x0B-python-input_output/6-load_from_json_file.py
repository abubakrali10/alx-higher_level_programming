#!/usr/bin/python3
""" ``load_from_json_file`` module
supplies 1 function, load_from_json_file(filename):
"""
import json


def load_from_json_file(filename):
    """ creates an object from a json file """
    with open(filename, 'r', encoding="utf-8") as f:
        return json.loads(f.read())
