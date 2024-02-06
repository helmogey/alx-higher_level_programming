#!/usr/bin/python3
""" returns a list of lists of integers representing the Pascal’s triangle of n"""


def pascal_triangle(n):
    """
    Returns a list of lists representing the Pascal's triangle of n rows.

    Args:
        n (int): The number of rows in the Pascal's triangle.

    Returns:
        list: A list of lists representing the Pascal's triangle.
    """

    if n <= 0:
        return []  # Empty list for invalid input

    triangle = [[1]]  # Start with the first row

    for i in range(1, n):
        row = [1]  # Start each row with 1
        for j in range(1, i):
            # Calculate inner elements using the Pascal's formula
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)  # End each row with 1
        triangle.append(row)

    return triangle
