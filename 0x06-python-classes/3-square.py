#!/usr/bin/python3
"""
Module 2-square
Defines class Square with private attribute size
"""


class Square:
    """
    class Square definition

    Args:
        size: size of a side in square
    """
    __size = None

    def __init__(self, size=0):
        """
        Initializes square

        Attributes:
            size: size of a side of a square
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size ** 2
