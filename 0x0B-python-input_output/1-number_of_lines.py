#!/usr/bin/python3
'''task 0'''


def number_of_lines(filename=""):
    line_counter = 0
    with open(filename, encoding="utf-8") as f:
        for line in f:
            line_counter += 1

    return line_counter
