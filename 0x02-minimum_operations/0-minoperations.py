#!/usr/bin/python3


"""
minimum operations
"""


import math


def is_prime(n):
    max_ = math.floor(math.sqrt(n))
    for x in range(2, max_+1):
        if n % x == 0:
            return 'not prime'
    return 'prime'


def minOperations(n: int) -> int:
    """min ops"""
    if n <= 0:
        return 0
    elif n < 6:
        return n
    elif is_prime(n) is True:
        return n
    else:
        lst = []
        even = 5
        for x in range(6, n):
            if is_prime(x) == 'not prime':
                lst.append(x)
            else:
                pass
        for i in lst:
            if i % 2 == 0:
                c = i - 6
                d = c/2
        return int(d + even)
