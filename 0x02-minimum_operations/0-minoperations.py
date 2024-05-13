#!/usr/bin/python3
"""
In a text file, there is a single character H. Your text editor can 
execute only two operations in this file: Copy All and Paste. 
Given a number n, write a method that calculates the fewest number of 
operations needed to result in exactly n H characters in the file.
"""


def Paste(remainder, number_of_operations, number_of_h_copied, number_of_h_required):
    """
    Paste the copied text recursively until the desired number of characters is reached.

    Args:
    - remainder (int): The remaining number of 'H' characters needed to paste.
    - number_of_operations (int): The current number of operations performed.
    - number_of_h_copied (int): The number of 'H' characters currently copied.
    - number_of_h_required (int): The total number of 'H' characters required.

    Returns:
    - int: The fewest number of operations needed to result in exactly n H characters in the file.
    """
    remainder -= number_of_h_copied
    number_of_operations += 1

    if remainder == 0:
        return number_of_operations

    elif remainder < 0:
        return 0

    p = Paste(
        remainder,
        number_of_operations,
        number_of_h_copied,
        number_of_h_required,
    )
    c = CopyAll(
        remainder,
        number_of_operations,
        number_of_h_copied,
        number_of_h_required,
    )
    if p == 0 and c == 0:
        return 0
    elif p == 0:
        return c
    elif c == 0:
        return p
    else:
        return min(p, c)


def CopyAll(remainder, number_of_operations, number_of_h_copied, number_of_h_required):
    """
    Copy all the 'H' characters and recursively paste them until the desired number is reached.

    Args:
    - remainder (int): The remaining number of 'H' characters needed to paste.
    - number_of_operations (int): The current number of operations performed.
    - number_of_h_copied (int): The number of 'H' characters currently copied.
    - number_of_h_required (int): The total number of 'H' characters required.

    Returns:
    - int: The fewest number of operations needed to result in exactly n H characters in the file.
    """
    number_of_h_copied += number_of_h_copied
    number_of_operations += 1

    if number_of_h_copied == number_of_h_required:
        return number_of_operations

    if number_of_h_copied > number_of_h_required:
        return 0

    p = Paste(
        remainder,
        number_of_operations,
        number_of_h_copied,
        number_of_h_required,
    )
    c = CopyAll(
        remainder,
        number_of_operations,
        number_of_h_copied,
        number_of_h_required,
    )
    if p == 0 and c == 0:
        return 0
    elif p == 0:
        return c
    elif c == 0:
        return p
    else:
        return min(p, c)


def minOperations(n):
    """
    Calculates the fewest number of operations needed to result in exactly n H characters in the file.

    Args:
    - n (int): The desired number of 'H' characters in the file.

    Returns:
    - int: The fewest number of operations needed to result in exactly n H characters in the file.
    """
    if n <= 1:
        return 0

    c = CopyAll(n, 0, 1, n)
    p = Paste(n, 0, 1, n)

    if c == 0 and p == 0:
        return 0
    elif c == 0:
        return p
    elif p == 0:
        return c
    else:
        return min(c, p)
