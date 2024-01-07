#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if len(matrix) > 1:
        c  = len(matrix[0])
        r = len(matrix)
        for lst in range(r):
            for ele in range(c - 1):
                print("{:d}".format(matrix[lst][ele]), end = " ")
            print("{:d}$".format(matrix[lst][c -1]), end="\n")
    else:
        print("$")
