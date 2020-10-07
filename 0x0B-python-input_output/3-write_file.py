#!/usr/bin/python3
'''task 3'''


def write_file(filename="", text=""):
    '''write in a file'''
    word_counter = 0
    with open(filename, 'w', encoding="UTF-8") as f:
        word_counter = f.write(text)
    return word_counter
