#!/usr/bin/python3
"""A method that calculates the fewest number of operations
needed to result in exactly n H characters in the file."""


def minOperations(n):
    """Calculates the fewest number of operations needed to result in exactly
    n H characters in the file and returns an integer 
    or returns 0 if n is impossible to achieve."""
    operations = 0
    min_operations = 2
    while n > 1:
        while n % min_operations == 0:
            operations += min_operations
            n /= min_operations
        min_operations += 1
    return operations
