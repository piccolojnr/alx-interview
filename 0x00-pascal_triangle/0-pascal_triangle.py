#!/usr/bin/python3
"""
Module 0-pascal_triangle
Contains function that returns lists of integers representing
Pascal’s triangle of n
"""


def pascal_triangle(n) -> list:
    """
    Returns a list of lists of integers representing the Pascal’s triangle of n
    """
    triangle = []

    if n <= 0:
        return triangle

    triangle.append([1])

    for i in range(1, n):
        tmp1 = []
        tmp2 = triangle[-1]

        for j in range(len(tmp2) + 1):
            f = tmp2[j - 1] if j - 1 >= 0 else 0
            l = tmp2[j] if j < len(tmp2) else 0
            tmp1.append(f + l)

        triangle.append(tmp1)

    return triangle
