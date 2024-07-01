#!/usr/bin/python3
"""Prime game find winner
"""


def isPrime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def removeMultiples(x, nums):
    return [n for n in nums if n % x != 0]


def playGame(n):
    nums = list(range(1, n + 1))
    turn = 0

    while True:
        primes = [num for num in nums if isPrime(num)]
        if not primes:
            break
        prime = primes[0]
        nums = removeMultiples(prime, nums)
        turn = 1 - turn

    return 1 - turn


def isWinner(x, nums):
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = playGame(n)
        if winner == 0:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
