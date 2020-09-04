#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv

    argc = len(argv)
    OPERATORS = "+-*/"
    functions = [add, sub, mul, div]
    a = int(argv[1])
    operator = argv[2]
    b = int(argv[3])
    f_idx = OPERATORS.find(operator)

    if argc != 4:
        print("Usage: {} <a> <operator> <b>".format(argv[0]))
        exit(1)
    if len(operator) != 1 or f_idx == -1:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    print(*argv[1:], end=" = ")
    print("{:d}".format(functions[f_idx](a, b)))
