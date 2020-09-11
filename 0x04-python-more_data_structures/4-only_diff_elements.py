#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    out = []
    for item in set_1:
        if item not in set_2:
            out.append(item)
    for item in set_2:
        if item not in set_1:
            out.append(item)
    return out
