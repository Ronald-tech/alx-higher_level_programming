#!/usr/bin/python3
'''Module for base class'''
from json import dumps, loads


class Base:
    ''' A representation of the base of our OOP hierarchy'''

    __nb_objects = 0

    def __init__(self, id=None):
        '''Constructor'''
        
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''Json is converting dictionary to be rightly longer'''
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return dumps(list_dictionaries)
