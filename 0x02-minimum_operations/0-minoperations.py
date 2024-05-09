#!/usr/bin/python3
"""
Calculates the fewest number of operations needed to result in exactly n H characters in the file.
"""

def minOperations(n):
    """
    Calculates the fewest number of operations needed to result in exactly n H characters in the file.

    Args:
        n (int): The number of H characters to achieve.

    Returns:
        int: The fewest number of operations needed.
    """
    if n <= 1:
        return 0
    
    for i in range(2, n + 1):
        if n % i == 0:
            return minOperations(n // i) + i
    return n

if __name__ == "__main__":
    n = 4
    print("Min number of operations to reach {} characters: {}".format(n, minOperations(n)))

    n = 12
    print("Min number of operations to reach {} characters: {}".format(n, minOperations(n)))

