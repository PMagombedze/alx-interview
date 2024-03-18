#!/usr/bin/python3


"""
prime game
"""


def isWinner(x, nums):
    """
    This function determines the winner of a game
    played by Maria and Ben based on the number of rounds(x)
    and the starting numbers (nums) in each round.
    """
    maria_wins = 0
    ben_wins = 0
    for num in nums:
        if num % 2 == 0:
            ben_wins += 1
        else:
            if num > 3:
                maria_wins += 1
            else:
                ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
