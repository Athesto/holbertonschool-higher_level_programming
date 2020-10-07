#!/usr/bin/python3
'''task 4'''


def inherits_from(obj, a_class):
    '''inherits'''
    return type(obj) is not a_class and isinstance(obj, a_class)
