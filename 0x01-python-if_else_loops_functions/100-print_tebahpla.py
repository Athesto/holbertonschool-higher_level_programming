#!/usr/bin/python3
for i in range(-25, 1):
    print("{:c}".format(ord('a' if i % 2 else 'A') + abs(i)), end="")
