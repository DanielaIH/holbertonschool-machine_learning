#!/usr/bin/env python3
"""function that calculates a series"""


def summation_i_squared(n):
    """summation i squared"""
    if n <= 1:
        return (n ** 2)
    else:
        return (n ** 2) + summation_i_squared(n - 1)
