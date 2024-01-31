#!/usr/bin/python3
"""
Defines class Rectangle
"""


class Rectangle:
    """Representation of a Rectangle"""
    def __init__(self, width=0, hieght=0):
        """Initializes the Rectangle"""
    self.hieght = hieght
    self.width = width

    @property
    def width(self):
        """getter for the private instance attribute width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for the private instance attribute width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def hieght(self):
        """getter for the private instance attribute hieght"""
        return self.__hiegtht

    @hieght.setter
    def hieght(self, value):
        """setter for the private instance attribute hieght"""
        if type(value) is not int:
            raise TypeError("hieght must be an integer")
        if value < 0:
            raise ValueError("hieght must be >= 0")
        self.__hieght = value
