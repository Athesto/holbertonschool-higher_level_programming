#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if len(matrix[0]) is 0:
        print()
        return
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if col == len(matrix[0]) - 1:
                print("{:d}".format(matrix[row][col]), end="")
            else:
                print("{:d}".format(matrix[row][col]), end=" ")
        print()
