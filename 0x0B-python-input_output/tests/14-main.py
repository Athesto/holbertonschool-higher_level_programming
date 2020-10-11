#!/usr/bin/python3
"""
14-main
"""
__import__('sys').path.append('.')
pascal_triangle = __import__('14-pascal_triangle').pascal_triangle


def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))


if __name__ == "__main__":
    print("----0----")
    print_triangle(pascal_triangle(0))
    print("----1----")
    print_triangle(pascal_triangle(1))
    print("----5----")
    print_triangle(pascal_triangle(5))
    print("----10----")
    print_triangle(pascal_triangle(10))
