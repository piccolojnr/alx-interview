#!/usr/bin/python3
"""
Making Change
"""

from typing import List
    
def makeChange(coins: List, total: int) -> int:
    """
    Given a pile of coins of different values, determine the fewest number of coins needed to meet a given amount total.
    """
    if total <= 0:
        return 0
    coins.sort(reverse=True)
    count = 0
    for coin in coins:
        count += total // coin
        total %= coin
    if total != 0:
        return -1
    return count