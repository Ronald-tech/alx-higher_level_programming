#!/usr/bin/python3
'''Module for Rectangle class.'''
Rectangle = __import__('9-base_geometry').Rectangle


class Square(Rectangle):
    '''A subclass representing a Rectangle.'''
    def __init__(self, size):
        '''Constructor.'''
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        '''Method for area of square.'''
        return self.__size ** 2
