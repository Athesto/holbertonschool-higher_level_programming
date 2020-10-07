#!/usr/bin/python3
'''advanced 100'''


class MyInt(int):
    '''inverted operators'''
    def __init__(self, value):
        '''constructor'''
        self.__value = value

    def __ne__(self, num):
        '''not equal operator'''
        return self.__value == num

    def __eq__(self, num):
        '''equal operator'''
        return self.__value != num
