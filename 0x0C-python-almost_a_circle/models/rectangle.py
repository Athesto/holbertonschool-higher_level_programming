#!/usr/bin/python3
'''rectangle module'''
from models.base import Base


class Rectangle(Base):
    '''Rectangle class'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''constructor'''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        '''getter'''
        return self.__width

    @property
    def height(self):
        '''getter'''
        return self.__height

    @property
    def x(self):
        '''getter'''
        return self.__x

    @property
    def y(self):
        '''getter'''
        return self.__y

    @width.setter
    def width(self, value):
        '''setter'''
        # TODO: validation
        if type(value) is not int:
            return Rectangle.raise_TypeError('width')
        self.__width = value

    @height.setter
    def height(self, value):
        '''setter'''
        if type(value) is not int:
            return Rectangle.raise_TypeError('height')
        # TODO: validation
        self.__height = value

    @x.setter
    def x(self, value):
        '''setter'''
        # TODO: validation
        self.__x = value

    @y.setter
    def y(self, value):
        '''setter'''
        # TODO: validation
        self.__y = value

    @staticmethod
    def raise_TypeError(attr):
        raise TypeError("{} must be an integer".format(attr))