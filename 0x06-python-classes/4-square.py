#!/usr/bin/python3
'''excercise 4'''


class Square:
    '''class square'''

    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        '''getSize'''
        return self.__size

    @size.setter
    def size(self, value):
        '''setSize'''
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        '''check area'''
        return (self.__size) ** 2
