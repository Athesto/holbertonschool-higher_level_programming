#!/usr/bin/python3
'''task 11'''
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    '''Square'''
    def __init__(self, size):
        '''constructor'''
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def __str__(self):
        '''print square'''
        return "[Square] {}/{}".format(self.__size, self.__size)
