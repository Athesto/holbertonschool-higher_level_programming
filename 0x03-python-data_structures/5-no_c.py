#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    for s_idx in range(len(my_string)):
        if my_string[s_idx] != 'c' and my_string[s_idx] != 'C':
                new_string += my_string[s_idx]
    return new_string
