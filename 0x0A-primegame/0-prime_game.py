#!/usr/bin/python3


"""
Prime game
"""


def isWinner(x, nums):
    """check for winner: ben/maria"""

    def canWin(num):
        """determine if can win"""
        if num == 1:
            return False
        if num == 2:
            return True
        if num % 2 == 0:
            return False
        return True

    countMaria = 0
    countBen = 0

    for n in nums:
        determineWin = canWin(n)
        if determineWin:
            if n % 2 == 0:
                countMaria += 1
            else:
                countBen += 1

    if countMaria > countBen:
        return "Maria"
    elif countBen > countMaria:
        return "Ben"
    else:
        return "None"
