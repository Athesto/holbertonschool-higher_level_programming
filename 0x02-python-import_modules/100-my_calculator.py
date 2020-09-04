#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv

    argc = len(argv)
    if argc != 4:
        print("Usage: {} <a> <operator> <b>".format(argv[0]))
        exit(1)

    functions = ["+-*/", [add, sub, mul, div]]
    a = int(argv[1])
    b = int(argv[3])
    operator = argv[2]
    f_idx = functions[0].find(operator)

    if len(operator) != 1 or f_idx == -1:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    print("{} {} {}".format(a, operator, b), end=" = ")
    print("{:d}".format(functions[1][f_idx](a, b)))
