#!/usr/bin/python3
'''move square'''


class Square:
    '''Square class'''

    def __init__(self, size=0, position=(0, 0)):
        self.size(size)
        self.position(position)

    def size(self):
        '''getter'''
        return self.__size

    def size(self, value):
        '''setter'''
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def position(self):
        '''getter'''
        return self.__position

    def position(self, value):
        if type(value) is not tuple or len(value) is not 2 or \
                any(list(map(lambda x: x < 0 or type(x) is not int, value))):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        '''calculation area'''
        return self.__size ** 2

    def my_print(self):
        '''printSquare, translated'''
        if self.__size is 0:
            print()
            return
        print("\n" * self.__position[1], end="")
        for row in range(self.__size):
            print(" " * self.__position[0], end="")
            print("#" * self.__size)
