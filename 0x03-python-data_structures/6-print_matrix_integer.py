#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for lst in matrix:
        for i, ele in enumerate(lst):
            if i < len(lst)- 1:
                print("{:d}".format(ele), end=" ")
            elif i == len(lst) - 1:
                print("{:d}".format(ele), end="")

        print("$")
