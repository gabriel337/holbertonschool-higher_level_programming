#!/usr/bin/python3
"""
Module 3-is_kind_of_class
Contains method is_kind_of_class
returns True if object is instance of class that it inherited from
"""


def is_kind_of_class(obj, a_class):
    """
    Return: True if obj is an instance of a class
    """
    return isinstance(obj, a_class)
