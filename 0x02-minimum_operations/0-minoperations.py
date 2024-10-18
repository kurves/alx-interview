#!/usr/bin/python3
"""
This module defines a function to calculate the minimum
needed to get exactly n characters 'H' in a text file.
"""


def minOperations(n):
    """
    Calculates the fewest number of operations needed.
    """
    if n <= 1:
        return 0
    operations = 0
    divisor = 2

    # Factorize the number n and count the operations needed
    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations
