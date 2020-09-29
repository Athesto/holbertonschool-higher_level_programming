#!/usr/bin/python3
'''Module task 3'''


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
    def width(self, value):
        '''setter'''
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        '''getter'''
        return self.__height

    @height.setter
    def height(self, value):
        '''setter'''
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        '''area'''
        return self.height * self.width

    def perimeter(self):
        '''perimeter'''
        if self.height is 0 or self.width is 0:
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self):
        out = "#" * self.width + '\n'
        out = out * self.height
        out = out[:-1]
        return out
