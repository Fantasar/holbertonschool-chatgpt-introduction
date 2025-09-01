#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function: Compute the factorial of a number recursively.

    Parameters:
    n (int): The non-negative integer for which to compute the factorial.

    Returns:
    int: The factorial of the input number n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


# Convert the first command-line argument to integer and calculate factorial
f = factorial(int(sys.argv[1]))
print(f)
