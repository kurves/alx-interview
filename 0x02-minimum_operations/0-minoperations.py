#!/usr/bin/python3
"""
Module for calculating the minimum operations needed
to result in exactly n 'H' characters in the file.
"""

def minOperations(n):
    """
    Calculates the fewest number of operations needed
    Returns:
    int: The minimum number of operations required.
    """
    if n <= 1:
        return 0

    operations = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    return operations
