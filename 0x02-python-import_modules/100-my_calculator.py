#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv

    #check if are there 3 args (1 cmd + 3 args)
    argc = len(argv)
    if argc != 4:
        print("Usage: {} <a> <operator> <b>".format(argv[0]))
        exit(1)

    # funtions[0] = operators' string
    # function[1][n] = functions imported
    functions = ["+-*/", [add, sub, mul, div]]
    a = int(argv[1])
    b = int(argv[3])
    operator = argv[2]

    # Search the operator inside operators string. Return it index
    # functions[0] = operators string
    f_idx = functions[0].find(operator)

    # check if operator is not a char OR
    # check if operator was not a found
    if len(operator) != 1 or f_idx == -1:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    print("{} {} {}".format(a, operator, b), end=" = ")

    # call add/sub/mul/div with input (a,b)
    print("{:d}".format(functions[1][f_idx](a, b)))
