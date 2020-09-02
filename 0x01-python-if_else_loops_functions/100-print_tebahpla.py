#!/usr/bin/python3
for i in range(26, 0, -1):
    print("{:c}".format(ord('A' if i % 2 else 'a') + i - 1), end="")
