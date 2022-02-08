#!/usr/bin/python3
"""
Module rectangle contains rectangle class

methods:
    def __init__(self, width, height, x=0, y=0, id inherited form BASE)
"""
from models.base import Base


class Rectangle(Base):
    """ def __init__ with attr width, height, x, y, id """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ initialize width, height, x and y """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ Getter returns width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter sets width """
        if type(value) is not int:
            raise TypeError("width must be an integer")

        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        """ Getter returns height """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter sets height """
        if type(value) is not int:
            raise TypeError("height must be an integer")

        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ Getter returns x """
        return self.__x

    @x.setter
    def x(self, value):
        """ Setter sets x """
        if type(value) is not int:
            raise TypeError("x must be an integer")

        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ Getter returns y """
        return self.__y

    @y.setter
    def y(self, value):
        """ Setter sets y """
        if type(value) is not int:
            raise TypeError("y must be an integer")

        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ returns area of rectangle by mult width * height """
        return self.__width * self.__height

    def display(self):
        """ prints rectangle with #'s """
        for y in range(self.y):
            print()
        for columns in range(self.height):
            for x in range(self.x):
                print(" ", end="")
            for rows in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        """ returns id, x, y , width and height """
        return("[Rectangle] ({}) {}/{} - {}/{}"
               .format(self.id, self.x, self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        """ adds input to arguments """
        if len(args) > 0:
            try:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
                self.y = args[4]
            except:
                pass
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
