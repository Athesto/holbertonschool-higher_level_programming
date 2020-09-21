#!/usr/bin/bash
def safe_print_list(my_list=[], x=0):
    counter = 0
    try:
        for idx in range(x):
            print(my_list[idx], end="")
            counter += 1
    except IndexError:
        pass
    print()
    return counter
