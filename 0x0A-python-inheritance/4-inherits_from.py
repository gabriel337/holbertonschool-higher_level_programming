#!/usr/bin/python3
"""
Module 4-inherits_from
Contains method 4-inherits_from
return True if obj is instance of class that it inherits from or is subclass
"""


def inherits_from(obj, a_class):
    """
    isinstance() to get class and any parent classes
    issubclass() to get what object is a subclass

    Return:
        True if obj is instance of class that it inherits from or is subclass
    """
    return issubclass(type(obj), a_class) and (type(obj) is not a_class)
