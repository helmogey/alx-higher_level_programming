#!/usr/bin/python3
def matrix_divided(matrix, div):
    res = []
    if not (isinstance(matrix, list) and all(isinstance(sublist, list) for sublist in matrix)  and all(all(isinstance(item, (int, float)) for item in sublist) for sublist in matrix)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if len(set(len(row) for row in matrix)) != 1:
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    for lst in matrix:
        tmp = []
        for elemnt in lst:
            tmp.append(round(elemnt/div, 2))
        res.append(tmp)
    return res
