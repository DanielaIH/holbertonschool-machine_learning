#!/usr/bin/env python3
import math
"""class Poisson that represents a poisson distribution"""


class Poisson:
    """class Poisson"""
    def __init__(self, data=None, lambtha=1.):
        """class Poisson"""
        if data is None:
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            self.lambtha = float(lambtha)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.lambtha = float(sum(data)) / len(data)

    def pmf(self, k):
        k = int(k)
        if k < 0:
            return 0
        else:
            return ((self.lambtha ** k) *
                    (math.exp(-self.lambtha)) / math.factorial(k))
