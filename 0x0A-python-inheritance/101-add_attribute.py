#!/usr/bin/python3
'''advanced 101'''


def add_attribute(obj, attribute, value):
    '''add attribute'''

    # print(dir(obj))
    if '__dict__' not in dir(obj):
        raise TypeError("can't add new attribute")
    setattr(obj, attribute, value)
