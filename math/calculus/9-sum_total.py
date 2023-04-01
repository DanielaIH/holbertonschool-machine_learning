#!/usr/bin/env python3
import numpy as np
"""function that calculates a series"""


def summation_i_squared(n):
    """summation i squared"""
    if type(n) is not int and n < 1:
        return None
    return sum(map(lambda n: n**2, range(n + 1)))
