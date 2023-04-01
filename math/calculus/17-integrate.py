#!/usr/bin/env python3
"""function that calculates the integral  of a polynomial"""


def poly_integral(poly, C=0):
    """integral  of a polynomial"""
    if type(poly) is not list or len(poly) <= 0 or type(C) is not int:
        return None
    if len(poly) == 1:
        return [0]
    return [C] + [(poly[i] / (i + 1)) for i in range(1, len(poly))]
