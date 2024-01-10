#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix:
        out = []
        for lst in matrix:
            tmp = []
            for l in lst:
                tmp.append(l**2)
            out.append(tmp)
        return out
