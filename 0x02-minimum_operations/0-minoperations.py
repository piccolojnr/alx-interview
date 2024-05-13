#!/usr/bin/python3
"""
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
"""


def minOperations(n):
    """
    :type n: int
    :rtype: int
    """
    if n <= 1:
        return 0
    if n % 2 == 0:
        return n // 2
    else:
        return n // 2 + 1
