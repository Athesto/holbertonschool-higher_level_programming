#!/usr/bin/python3
'''task 13'''


class Student():
    '''Student'''

    def __init__(self, first_name, last_name, age):
        ''''constructor'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''to_json'''
        if type(attrs) is list and all([type(item) is list for item in attrs]):
            out = dict()
            for key in list(set(self.__dict__) & set(attrs)):
                out[key] = self.__dict__[key]
            print(out)
            return out
        return self.__dict__

    def reload_from_json(self, json):
        '''reload'''
        if json != {}:
            self.__dict__ = json
