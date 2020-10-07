#!/usr/bin/python3
'''task 9'''
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    '''Rectangle'''
    def __init__(self, width, height):
        '''constructor'''
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        '''str ouput'''
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)

    def area(self):
        '''width * height'''
        return self.__width * self.__height
