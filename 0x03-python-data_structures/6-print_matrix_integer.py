#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not any(matrix):
        print()
        return
    for m_idx in range(len(matrix)):
        print("{} {} {}".format(*matrix[m_idx]))
