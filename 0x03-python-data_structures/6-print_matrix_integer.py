#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not any(matrix):
        print()
        return
    for m_idx in range(len(matrix)):
        print("{:d} {:d} {:d}".format(*matrix[m_idx]))
