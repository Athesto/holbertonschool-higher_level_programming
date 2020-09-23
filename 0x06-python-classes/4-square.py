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
        try:
            if type(value) is not int:
                raise TypeError
            elif value < 0:
                raise ValueError
            else:
                self.__size = value
        except TypeError:
            print("size must be an integer")
        except ValueError:
            print("size must be >= 0")

    def area(self):
        '''check area'''
        return (self.__size) ** 2
