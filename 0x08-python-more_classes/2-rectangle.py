#!/usr/bin/python3
'''Module task3'''


class Rectangle:
    '''Class Rectangle'''
    def __init__(self, width=0, height=0):
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
        return self.__height

    @height.setter
    def height(self, height):
        '''setter'''
        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = height

    def area(self):
        '''area'''
        return self.__height * self.__width

    def perimeter(self):
        '''perimeter'''
        if self.height is 0 or self.width is 0:
            return 0
        return 2 * (self.__height + self.__width)
