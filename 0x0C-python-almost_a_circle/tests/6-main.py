#!/usr/bin/python3
""" 6-main """
from models.rectangle import Rectangle
__import__("sys").path.append(".")


def main():

    if __name__ == "__main__":

        r1 = Rectangle(2, 3, 2, 2)
        r1.display()

        print("---")

        r2 = Rectangle(3, 2, 1, 0)
        r2.display()


main()