#!/usr/bin/python3
"""
Module to define isWineer function (Prime Game)
"""


def primes(n):
    """
    Return list of prime numbers between 1 and n inclusive
       Args:
        n (int): upper limit of range and 1 is always the lower limit
    """
    prime = []
    sieve = [True] * (n + 1)
    for p in range(2, n + 1):
        if (sieve[p]):
            prime.append(p)
            for i in range(p, n + 1, p):
                sieve[i] = False
    return prime


def isWinner(x, nums):
    """
    Function that determines winner of Prime Game
    Args:
        x (int): number of rounds of game
        nums (int): array of n
    Return:
        Name of winner or None if winner cannot be found
    """
    if x is None or nums is None or x == 0 or nums == []:
        return None
    Maria = Ben = 0
    for i in range(x):
        prime = primes(nums[i])
        if len(prime) % 2 == 0:
            Ben += 1
        else:
            Maria += 1
    if Maria > Ben:
        return 'Maria'
    elif Ben > Maria:
        return 'Ben'
    return None
