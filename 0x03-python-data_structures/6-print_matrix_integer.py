#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for lst in matrix:
        for i, ele in enumerate(lst):
            if i < len(lst):
                print("{:d}".format(ele), end=" ")
            else:
                print("")
        print()