#!/usr/bin/python3
"""
Module 7-base_geometry
Contains BaseGeometry
with public instance methods area and integer_validation
"""


class BaseGeometry:
    """
    Methods:
        area(self)
        integer_validator(self, name, value)
    """
    def area(self):
        """
        raises an exeption
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Checks for input
        """
        if not isinstance(value, int):
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
