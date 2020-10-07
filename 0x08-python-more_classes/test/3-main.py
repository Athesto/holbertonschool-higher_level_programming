#!/usr/bin/python3
Rectangle = __import__('3-rectangle').Rectangle

def main():
    my_rectangle = Rectangle(2, 4)
    print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

    print(str(my_rectangle))
    print(repr(my_rectangle))

    print("--")

    my_rectangle.width = 10
    my_rectangle.height = 3
    print(my_rectangle)
    print(repr(my_rectangle))
    print("usr tst")
    r = Rectangle()
    print(r.width)
    print(r.height)
    print(str(r))
    print(r)
    test(1,1)
    test([],1)
    test(-1,1)
    test(1,[])
    test(1,-1)


def test(a,b):
    try:
        Rectangle(a,b)
    except Exception as e:
        print("{}: {}".format(type(e).__name__, e))

main()
