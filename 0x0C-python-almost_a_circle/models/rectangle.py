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
        Rectangle.isInt('width', value)
        Rectangle.checkValue('width', value)
        self.__width = value

    @height.setter
    def height(self, value):
        '''setter'''
        Rectangle.isInt('height', value)
        Rectangle.checkValue('height', value)
        self.__height = value

    @x.setter
    def x(self, value):
        '''setter'''
        Rectangle.isInt('x', value)
        Rectangle.checkValue('x', value)
        self.__x = value

    @y.setter
    def y(self, value):
        '''setter'''
        Rectangle.isInt('y', value)
        Rectangle.checkValue('y', value)
        self.__y = value

    def area(self):
        '''area = width * height'''
        return self.width * self.height

    def display(self):
        '''dislpay the rectangle'''
        symbol = "#"
        out = ""
        out += symbol * self.width + '\n'
        out *= self.height
        out = out[:-1]
        print(out)

    @staticmethod
    def isInt(key, value):
        '''check if value is int'''
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(key))

    @staticmethod
    def checkValue(key, value):
        if value <= 0 and key in ('width', 'height'):
            raise ValueError("{} must be > 0".format(key))
        if value < 0 and key in ('x', 'y'):
            raise ValueError("{} must be >= 0".format(key))
