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


class Rectangle(BaseGeometry):
    """
    Methods:
        __init__(self, width, height)
    """
    def __init__(self, width, height):
        """ validates and initialize width and height"""

        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def __str__(self):
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))

    def area(self):
        """returns witdh * height"""
        return self.__width * self.__height


class Square(Rectangle):
    """
    Methods:
        __init__(self, size)
    """
    def __init__(self, size):
        """ Validates and initialize width and height"""
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
