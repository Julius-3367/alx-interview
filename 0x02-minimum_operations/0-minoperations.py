#!/usr/bin/python3
"""
Minimum Operations
"""

def minOperations(n: int) -> int:
    """
    Minimum Operations needed to get n H characters
    """
    if n <= 1:
        return 0
    
    op = 0
    copy = 1
    paste = 0

    while paste < n:
        if n % copy == 0:
            paste = copy
            op += 1
        copy += paste
        op += 1

    return op

if __name__ == "__main__":
    n = 4
    print("Min number of operations to reach {} characters: {}".format(n, minOperations(n)))

    n = 12
    print("Min number of operations to reach {} characters: {}".format(n, minOperations(n)))

