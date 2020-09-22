#!/usr/bin/python3
'''Excercise 2'''


class Square:
    '''Square with size review'''
    def __init__(self, size=0):
        try:
            self.__size = size
            if size < 0:
                raise ValueError("size must be >= 0")
        except TypeError:
            print("size must be an integer")
