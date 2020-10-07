#!/usr/bin/python3
Rectangle = __import__('1-rectangle').Rectangle


def main():
    my_rectangle = Rectangle(2, 4)
    print(my_rectangle.__dict__)

    my_rectangle.width = 10
    my_rectangle.height = 3
    print(my_rectangle.__dict__)

    print("usr tests")
    Rectangle()
    print(my_rectangle.width)
    print(my_rectangle.height)
    print("width")
    test(1.0,1)
    test([],1)
    test(True,1)
    test("hello",1)
    test(-1,1)

    print("height")
    test(1, [])
    test(1, 1.0)
    test(1, -1)


def test(width, height):
    try:
        a = Rectangle(width, height)
    except Exception as e:
        print("{}: {}".format(type(e).__name__, e))

main()
