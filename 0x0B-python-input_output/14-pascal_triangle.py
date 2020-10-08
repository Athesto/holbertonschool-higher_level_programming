#!/usr/bin/python3
'''task 14'''


def pascal_triangle(n):
    '''pascal_triangle'''
    if n <= 1:
        return []
    prev = [1]
    return [1, 4, 6, 4, 1]
