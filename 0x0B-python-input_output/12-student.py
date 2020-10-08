#!/usr/bin/python3
'''task 12'''


class Student():
    '''Student'''

    def __init__(self, first_name, last_name, age):
        '''constructor'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        out = dict()
        for key in list(set(attrs) & set(self.__dict__)):
            out[key] = self.__dict__[key]
        return out
