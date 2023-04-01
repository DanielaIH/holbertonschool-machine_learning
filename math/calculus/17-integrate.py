#!/usr/bin/env python3
"""function that calculates the integral  of a polynomial"""


def poly_integral(poly, C=0):
    """integral  of a polynomial"""
    if type(poly) is not list or len(poly) <= 0 or type(C) is not int:
        return None
    if len(poly) == 1:
        return [C, poly[0]]

    new_poly = []
    for i in range(len(poly)):
        integral = poly[i] / (i + 1)
        if (integral) % 1 == 0:
            integral = int(integral)
        new_poly.append(integral)
    return [C] + new_poly
