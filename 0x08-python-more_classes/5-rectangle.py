#!/usr/bin/python3
'''task 5'''


class Rectangle:
    '''Rectangle'''
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        '''constructor'''
        Rectangle.number_of_instances += 1
        self.width = width
        self.height = height

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @property
    def width(self):
        '''getter'''
        return self.__width

    @property
    def height(self):
        '''getter'''
        return self.__height

    @width.setter
    def width(self, width):
        '''setter'''
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width

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
        return self.height * self.height

    def perimeter(self):
        '''perimeter'''
        if self.width is 0 or self.height is 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        if self.width is 0 or self.height is 0:
            return ""
        out = "#" * self.width + '\n'
        out = out * self.height
        out = out[:-1]
        return out

    def __repr__(self):
        return "{}({}, {})".format(
                type(self).__name__,
                self.width,
                self.height
                )
