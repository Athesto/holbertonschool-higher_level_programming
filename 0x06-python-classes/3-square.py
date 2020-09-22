#!/usr/bin/python3
'''Area Square'''


class Square:
    '''Class Square'''

    def __init__(self, size=0):
        try:
            if size < 0:
                raise ValueError
            if type(size) is not int:
                raise TypeError
            self.__size = size
        except TypeError:
            print("size must be an integer")
        except ValueError:
            print("size must be >= 0")

    def area(self):
        '''square^2'''
        return self.__size * self.__size
