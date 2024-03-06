#!/usr/bin/python3


"""
coin problem
"""


def makeChange(coins, total):
    """make change"""
    num = float('inf')
    if total <= 0:
        return 0

    solutionSet = [float('inf')] * (total + 1)
    solutionSet[0] = 0

    for amount in range(1, total + 1):
        for coin in coins:
            sm = solutionSet[amount]
            if coin <= amount and solutionSet[amount - coin] + 1 < sm:
                solutionSet[amount] = solutionSet[amount - coin] + 1

    if solutionSet[total] == float('inf'):
        return -1

    return solutionSet[total]
