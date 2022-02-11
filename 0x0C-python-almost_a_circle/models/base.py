#!/usr/bin/python3
"""
Module base.py contains class Base with private atrr __nb_objects

Methods:
    def __init__(self, id=None)
"""

import json


class Base:
    """ Contains def __init__"""
    __nb_objects = 0

    def __init__(self, id=None):
        """ initializes id """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            Base.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ return the JSON string representation of list_dictionaries """
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ JSON string to file """
        with open(cls.__name__ + ".json", "w", encoding='utf8') as f:
            if list_objs is None:
                f.write("[]")
            else:
                empty_list = []
                for obj in list_objs:
                    empty_list.append(obj.to_dictionary())
                f.write(Base.to_json_string(empty_list))

    @staticmethod
    def from_json_string(json_string):
        """  JSON string to dictionary """
        emptylist = []
        if json_string is None:
            return emptylist
        else:
            return json.loads(json_string)
