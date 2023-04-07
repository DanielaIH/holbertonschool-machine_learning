#!/usr/bin/env python3
"""class Poisson that represents a poisson distribution"""


class Poisson:
    """class Poisson"""
    e = 2.7182818285

    def __init__(self, data=None, lambtha=1.):
        """class Poisson __init__"""
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
        """calculates the pmf"""
        k = int(k)
        factorial = 1
        if k < 0:
            return 0
        else:
            for i in range(1, k + 1):
                factorial *= i
            return ((self.lambtha ** k) *
                    (self.e ** -self.lambtha) / factorial)
