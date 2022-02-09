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
