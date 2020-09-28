#!/usr/bin/python3
'''module task 1'''


class Rectangle:
    '''Rectangle Class'''
    def __init__(self, width=0, height=0):
        '''constuctor'''
        self.width = width
        self.height = height

    @property
    def width(self):
        '''getter'''
        return self.__width

    @width.setter
    def width(self, width):
        '''setter'''
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width

    @property
    def height(self):
        '''getter'''
        return self.__heigth

    @height.setter
    def height(self, height):
        '''setter'''
        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise TypeError("height must be >= 0")
        else:
            self.__height = height
