#!/usr/bin/python3
'''task 2'''


def read_lines(filename="", nb_lines=0):

    with open(filename, encoding="utf-8") as f:
        counter = 0
        for line in f:
            print(line, end="")
            counter += 1
            if(nb_lines > 0 and counter == nb_lines):
                break
