#!/usr/bin/python3
'''remove'''


def remove_char_at(str, n):
    '''welcome'''
    out = ""
    for c in str:
        if n:
            out += c
        n -= 1
    return out
