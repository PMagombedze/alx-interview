#!/usr/bin/python3


"""
prime game
"""


def isPrime(num):
    """Check if a number is prime."""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def isWinner(x, nums):
    """determine winner"""
    countMaria = 0
    countBen = 0

    for n in nums:
        numbers = list(range(1, n + 1))
        maria_turn = True
        while numbers:
            prime = None
            for num in numbers:
                if isPrime(num):
                    prime = num
                    break
            if prime is None:
                if maria_turn:
                    countBen += 1
                else:
                    countMaria += 1
                break
            numbers = [num for num in numbers if num % prime != 0]
            maria_turn = not maria_turn

    if countMaria > countBen:
        return "Maria"
    elif countBen > countMaria:
        return "Ben"
    else:
        return None
