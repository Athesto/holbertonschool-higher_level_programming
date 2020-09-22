#!/usr/bin/python3
'''Excercise 2'''


class Square:
    '''Square with size review'''
    def __init__(self, size=0):
        try:
            if size < 0:
                raise ValueError("size must be >= 0")
            if type(size) != int:
                raise TypeError
            self.__size = size
        except TypeError:
            raise NameError("size must be an integer")
