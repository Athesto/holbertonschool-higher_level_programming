#!/usr/bin/python3
__import__('sys').path.append('.')

""" 0-main """


def main():
    from models.base import Base
    if __name__ == "__main__":

        b1 = Base()
        print(b1.id)

        b2 = Base()
        print(b2.id)

        b3 = Base()
        print(b3.id)

        b4 = Base(12)
        print(b4.id)

        b5 = Base()
        print(b5.id)


main()
