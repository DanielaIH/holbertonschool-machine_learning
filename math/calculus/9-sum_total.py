#!/usr/bin/env python3
"""function that calculates a series"""


def summation_i_squared(n):
    """summation i squared"""
    sum = 0
    for i in range(n):
        sum += ((i + 1) ** 2)
    return sum
