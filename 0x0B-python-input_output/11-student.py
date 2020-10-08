#!/usr/bin/python3
'''task 11'''


class Student():
    '''student'''

    def __init__(self, first_name, last_name, age):
        '''constructor'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        '''to_json'''
        return self.__dict__
