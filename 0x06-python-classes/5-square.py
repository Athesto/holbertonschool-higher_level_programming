#!/usr/bin/python3
'''Print Square'''


class Square:
    '''Square class'''
    def __init__(self, value):
        self.__size = value

    @property
    def size(self):
        '''getter'''
        return self.__size

    @size.setter
    def size(self, value):
        '''setter'''
        if value < 0:
            raise ValueError("size must be >= 0")
        elif type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            self.__size = value

    def area(self):
        '''area'''
        return self.__size ** 2

    def my_print(self):
        '''print squares'''
        if self.__size == 0:
            print()
        for row in range(self.__size):
            print(self.__size * "#")
