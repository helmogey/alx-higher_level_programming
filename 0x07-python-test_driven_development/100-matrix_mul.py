#!/usr/bin/python3
def matrix_mul(m_a, m_b):
    if not (isinstance(m_a, list)):
        raise TypeError("m_a must be a list")

    if not all(isinstance(sublist, list) for sublist in m_a):
        raise TypeError("m_a must be a list of lists")

    if not all(bool(len(item) > 0) for item in m_a):
        raise ValueError("m_a can't be empty")

    if not all(all(isinstance(item, (int, float)) for item in sublist) for sublist in m_a):
        raise TypeError("m_a should contain only integers or floats")


    if len(set(len(row) for row in m_a)) != 1:
        raise TypeError("each row of m_a must be of the same size")

    if not (isinstance(m_b, list)):
        raise TypeError("m_b must be a list")

    if not all(isinstance(sublist, list) for sublist in m_b):
        raise TypeError("m_b must be a list of lists")

    if not all(bool(len(item) > 0) for item in m_b):
        raise ValueError("m_b can't be empty")

    if not all(all(isinstance(item, (int, float)) for item in sublist) for sublist in m_b):
        raise TypeError("m_b should contain only integers or floats")


    if len(set(len(row) for row in m_b)) != 1:
        raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    Transposed = []
    for r in range(len(m_b[0])):
        new_row = []
        for c in range(len(m_b)):
            new_row.append(m_b[c][r])
        Transposed.append(new_row)

    Res = []
    for row in m_a:
        new_row = []
        for col in Transposed:
            prod = 0
            for i in range(len(Transposed[0])):
                prod += row[i] * col[i]
            new_row.append(prod)
        Res.append(new_row)

    return Res

