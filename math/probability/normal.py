#!/usr/bin/env python3
"""class Normal that represents a normal distribution"""


class Normal:
    """class Normal"""

    def __init__(self, data=None, mean=0., stddev=1.):
        """class Normal __init__"""
        if data is None:
            if stddev <= 0:
                raise ValueError("stddev must be a positive value")
            self.stddev = float(stddev)
            self.mean = float(mean)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.mean = sum(data) / len(data)
            self.stddev = (sum((x - self.mean) ** 2 for x in data)
                           / (len(data) - 1)) ** (0.5)

    def pdf(self, x):
        """lambda e^{{-lambda x}}"""
        if x < 0:
            return 0
        else:
            return self.lambtha * (self.e ** (- self.lambtha * x))

    def cdf(self, x):
        """{ 1-e^{-lambda x}}"""
        if x < 0:
            return 0
        else:
            return 1 - (self.e ** (- self.lambtha * x))
