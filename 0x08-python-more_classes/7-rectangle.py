#!/usr/bin/python3
"""
Defines class Rectangle
"""


class Rectangle:
    """Representation of a Rectangle"""

    number_of_instances = 0
    """int: The number of active instances."""
    
    print_symbol = "#"
    """type: Print symbol, can be any type."""

    def __init__(self, width=0, height=0):
        """Constructor

        Args:
            width: The width of Rectangle.
            height: The hieght of the Rectangle.
        """
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

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
    def height(self):
        """getter for the private instance attribute height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for the private instance attribute height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of the Rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Returns perimeter of the Rectangle"""
        if not self.width or not self.height:
            return 0
        return (self.width + self.height) * 2

    def __str__(self):
        """Returns printable string representation of the rectangle"""
        if not self.width or not self.height:
            return ""
        return ((str(self.print_symbol) * self.width + "\n") *
                self.height)[:-1]

    def __repr__(self):
        """Returns string representation for a Rectangle for reproduction"""
        return "Rectangle(" + str(self.width) + ", " + str(self.height) + ")"
    def __del__(self):
        """Prints a string  when an instance has been deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
