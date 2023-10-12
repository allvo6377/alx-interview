#!/usr/bin/python3
"""Module to implement 0-miniOperations function"""


def minOperations(n):
    """
    Calculates the fewest number of operations needed to result in exactly n H characters in the file.

    Args:
        n (int): The desired number of H characters.

    Returns:
        int: The fewest number of operations needed to result in exactly n H characters in the file.
             If n is impossible to achieve, returns 0.
    """
    operations = 0
    if n <= 1:
        return operations
    while n > 1:
        if n % 2 == 0:
            n //= 2
            operations += 2
        else:
            for i in range(3, n + 1, 2):
                if n % i == 0:
                    n //= i
                    operations += i
                    break
    return operations
