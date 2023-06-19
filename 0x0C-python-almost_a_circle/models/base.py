#!/usr/bin/python3
"""
''Base'' module
"""
import json


class Base:
    """ a Base class for all other shapes """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initializing the Base """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects = Base.__nb_objects + 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Returns a json string representation of a dict list """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """ returns the list of the JSON string representation """
        if json_string is None or len(json_string) == 0:
            return "[]"
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the JSON string representation of objects to a file
        """
        with open(f'{cls.__name__}.json', 'w') as f:
            if list_objs is None:
                f.write("[]")
            else:
                objs_dict = []
                for obj in list_objs:
                    objs_dict.append(obj.to_dictionary())
                f.write(Base.to_json_string(objs_dict))
