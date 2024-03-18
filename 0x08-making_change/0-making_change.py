#!/usr/bin/python3


"""
coin problem
"""


def makeChange(coins, total):
    """
    This function determines the fewest number of
    coins needed to meet a given amount.
    """
    min_coins = [float('inf')] * (total + 1)
    min_coins[0] = 0
    for amount in range(1, total + 1):
        for coin in coins:
            if coin <= amount:
                new_coins = min_coins[amount - coin] + 1
                min_coins[amount] = min(min_coins[amount], new_coins)

    return min_coins[total] if min_coins[total] != float('inf') else -1
