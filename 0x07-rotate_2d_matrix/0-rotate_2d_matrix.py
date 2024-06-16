#!/usr/bin/python3
"""
Rotate
    """


def rotate_2d_matrix(matrix):
    """_summary_

    Args:
        matrix (_type_): _description_
    """
    n = len(matrix)

    # Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row
    for i in range(n):
        matrix[i].reverse()
