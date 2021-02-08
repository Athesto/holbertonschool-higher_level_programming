#!/usr/bin/python3
def uppercase(str):
    out = ""
    for c in str:
        if ('a' <= c <= 'z') or ('A' <= c <= 'Z'):
            out += "{:c}".format(ord(c) & ord('_'))
        else:
            out += c
    print(out)
