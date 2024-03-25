#!/usr/bin/python3


"""
prime game
"""


def isWinner(x, nums):
    """
    Evaluates the winner of a prime game
    """
    if x < 1 or not nums:
        return None
    mariasWins, bensWins = 0, 0
    n = max(nums)
    primes = [True] * n
    primes[0] = False
    for i in range(2, int(n ** 0.5) + 1):
        if primes[i - 1]:
            for j in range(i * i, n + 1, i):
                primes[j - 1] = False
    for n in nums:
        primesCount = sum(1 for prime in primes[:n] if prime)
        bensWins += primesCount % 2 == 0
        mariasWins += primesCount % 2 == 1
    if mariasWins == bensWins:
        return None
    return 'Maria' if mariasWins > bensWins else 'Ben'
