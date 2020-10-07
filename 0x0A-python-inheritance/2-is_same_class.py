#!/usr/bin/python3
'''module task2'''


def is_same_class(obj, a_class):
    '''function is_same_class'''
    return type(obj) is a_class
    # return type(obj).__name__ ==  a_class.__name__
