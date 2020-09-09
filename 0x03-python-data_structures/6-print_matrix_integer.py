#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if len(matrix[0]) is 0:
        print()
        return
    for m_idx in range(len(matrix)):
        print("{:d} {:d} {:d}".format(*matrix[m_idx]))
