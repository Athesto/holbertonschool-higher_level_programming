#!/usr/bin/python3
'''task 14'''


def pascal_triangle(n):
    '''pascal_triangle'''
    if n <= 0:
        return []
    out = []
    prev = [1]
    new = prev[:]
    out.append(new[:])
    for x in range(n - 1):
        for y in range(len(prev)):
            if y is 0:
                continue
            new[y] = prev[y] + prev[y - 1]
        new.append(1)
        prev = new[:]
        out.append(new[:])
    return out
