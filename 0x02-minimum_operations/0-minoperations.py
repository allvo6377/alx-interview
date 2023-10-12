#!/usr/bin/python3
"""Module to implement 0-miniOperations function"""


def minOperations(n):
    """
    Calculate the minimum number of operations needed to get exactly n 'H' characters in the file.

    Parameters:
    n (int): The target number of 'H' characters.

    Returns:
    int: The minimum number of operations needed. If n is impossible to achieve, return 0.
    """
    
    if n == 1:
        return 0

    dp = [0] * (n + 1)
    dp[1] = 0

    for i in range(2, n + 1):
        dp[i] = i
        for j in range(i - 1, 0, -1):
            if i % j == 0:
                dp[i] = min(dp[i], dp[j] + 2 * (i // j))
                break

    return dp[n]
