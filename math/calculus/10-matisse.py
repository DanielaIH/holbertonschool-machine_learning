#!/usr/bin/env python3
"""function that calculates the derivative of a polynomial"""


def poly_derivative(poly):
    """derivative of a polynomial"""
    if type(poly) is not list or len(poly) <= 0:
        return None
    return [poly[i] * i for i in range(poly)]
