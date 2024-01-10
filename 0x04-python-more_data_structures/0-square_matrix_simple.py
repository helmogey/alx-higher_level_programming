#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix:
        out = []
        for lst in matrix:
            out.append(list(map(lambda x: x ** 2, lst)))
        return out
