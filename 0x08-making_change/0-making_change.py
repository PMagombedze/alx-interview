#!/usr/bin/python3


"""
coin problem
"""


def makeChange(coins, total):
    """make change"""
    num = float('inf')
    solutionSet = [num] * (total + 1)
    solutionSet[0] = 0
    for coin in coins:
        for amount in range(coin, total + 1):
            solutionSet[amount] = min(
                solutionSet[amount], solutionSet[amount - coin] + 1
            )
    if total <= 0:
        return 0
    if solutionSet[total] == num:
        return -1
    else:
        return solutionSet[total]
