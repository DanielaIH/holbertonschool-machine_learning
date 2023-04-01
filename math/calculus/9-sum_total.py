#!/usr/bin/env python3
"""function that calculates a series"""


def summation_i_squared(n):
    """summation i squared"""
    if not n:
        return None
    if n <= 1:
        return n
    else:
        return (n ** 2) + summation_i_squared(n - 1)


a = summation_i_squared(5)
print(a)