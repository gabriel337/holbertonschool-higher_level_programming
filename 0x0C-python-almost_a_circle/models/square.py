#!/usr/bin/python3
"""
Module square contains class Square
    methods:
    def __init__
    def __str__
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ contains: __init__ with att: size, x, y and id) and __str__ """
    def __init__(self, size, x=0, y=0, id=None):
        """ initialize size, x, y and id with Rectangle class """
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """ getter returns size """
        return self.width

    @size.setter
    def size(self, value):
        """ setter sets size """
        if type(value) is not int:
            raise TypeError("width must be an integer")

        if value <= 0:
            raise ValueError("width must be > 0")

        self.width = value
        self.height = value

    def __str__(self):
        """ returns id, x, y , width and height """
        return ("[Square] ({}) {}/{} - {}"
                .format(self.id, self.x, self.y, self.size, self.size))

    def update(self, *args, **kwargs):
        """ adds input to arguments """
        ls = ['id', 'size', 'x', 'y']
        if args:
            for idx in range(len(args)):
                setattr(self, ls[idx], args[idx])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ returns Square instance to dictionary representation """
        return {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}
