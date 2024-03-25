#!/usr/bin/python3


"""
prime game
"""


def sieve_of_eratosthenes(n):
    """Sieve of Eratosthenes algorithm to find all primes less than n."""
    prime = [True for _ in range(n+1)]
    p = 2
    while (p * p <= n):
        p_ = prime[p]
        if p_ is True:
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1
    primes = [p for p in range(2, n+1) if prime[p]]
    return primes


def isWinner(x, nums):
    """Determine the winner of the prime game."""
    maria_wins = 0
    ben_wins = 0
    for n in nums:
        primes = sieve_of_eratosthenes(n)
        turn = 'Maria'
        while primes:
            prime = primes.pop(0)
            primes = [num for num in primes if num % prime != 0]
            turn = 'Ben' if turn == 'Maria' else 'Maria'
        if turn == 'Maria':
            ben_wins += 1
        else:
            maria_wins += 1
    if maria_wins > ben_wins:
        return 'Maria'
    elif ben_wins > maria_wins:
        return 'Ben'
    else:
        return None
