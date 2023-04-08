#!/usr/bin/env python3
"""class Normal that represents a normal distribution"""


class Normal:
    """class Normal"""
    e = 2.7182818285
    pi = 3.141592653

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
            self.mean = float(sum(data)) / len(data)
            self.stddev = (sum((x - self.mean) ** 2 for x in data)
                           / len(data)) ** (0.5)

    def z_score(self, x):
        """calculates z score"""
        return (x - self.mean) / self.stddev

    def x_value(self, z):
        """calculates x value"""
        return self.mean + z * self.stddev

    def pdf(self, x):
        """calculates pdf"""
        exp = (-(x - self.mean) ** 2) / (2 * self.stddev ** 2)
        num = self.e ** (exp)
        den = self.stddev * (2 * self.pi) ** 0.5
        return float(num / den)

    def erf(self, x):
        """calculates error"""
        x1 = 2 / self.pi ** 0.5
        x2 = x - (x**3 / 3) + (x**5 / 10) - (x**7 / 42) + (x**9 / 216)
        return x1 * x2

    def cdf(self, x):
        """calculates cdf"""
        z = (x - self.mean) / (self.stddev * (2 ** 0.5))
        return (self.erf(z) + 1) / 2
