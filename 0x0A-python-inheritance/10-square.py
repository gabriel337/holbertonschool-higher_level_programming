#!/usr/bin/python3
"""
Module 10-rectangle
Contains parent class BaseGeometry
with public instance method area and integer_validator
Contains subclass Rectangle
with instantiation of private attributes width and height, validated by parent
contains subclass Square
with instantiation of private attribute size.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Methods:
        __init__(self, size)
    """
    def __init__(self, size):
        """ Validates and initialize width and height"""
        self.__size = size
        super().integer_validator("size", size)
        super().integer_validator("size", size)
        super().__init__(size, size)
