#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    out = []
    for item in set_1:
        if item not in set_2:
            out.append(item)
    return out
