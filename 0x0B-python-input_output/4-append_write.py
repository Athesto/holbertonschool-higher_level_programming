#!/usr/bin/python3
'''task 4'''


def append_write(filename="", text=""):
    '''append to file'''
    word_counter = 0
    with open(filename, 'a', encoding="UTF-8") as f:
        word_counter = f.write(text)
    return word_counter
