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

    @width.setter
    def width(self, value):
        '''setter'''
        # TODO: validation
        self.__width = value

    @property
    def height(self):
        '''getter'''
        return self.__height

    @height.setter
    def height(self, value):
        '''setter'''
        # TODO: validation
        self.__height = value

    @property
    def x(self):
        '''getter'''
        return self.__x

    @x.setter
    def x(self, value):
        '''setter'''
        # TODO: validation
        self.__x = value

    @property
    def y(self):
        '''getter'''
        return self.__y

    @y.setter
    def y(self, value):
        '''setter'''
        # TODO: validation
        self.__y = value
