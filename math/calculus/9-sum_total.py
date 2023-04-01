#!/usr/bin/env python3
"""function that calculates a series"""


def summation_i_squared(n):
    """summation i squared"""
    if type(n) is not int or n < 1:
        return None
    return sum(map(lambda n: n**2, range(n + 1)))
