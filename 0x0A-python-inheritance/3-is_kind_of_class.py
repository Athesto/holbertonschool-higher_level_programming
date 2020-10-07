#!/usr/bin/python3
'''task 3'''


def is_kind_of_class(obj, a_class):
    '''is_kind of class'''
    return isinstance(obj, a_class)
    # return type(obj) is a_class or \
    #       type(obj).__base__ is a_class
    # return type(obj).__name__ == a_class.__name__ or\
    #        type(obj).__base__.name == a_class.__name
