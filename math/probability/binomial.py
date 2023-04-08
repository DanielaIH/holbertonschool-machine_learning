#!/usr/bin/env python3
"""class Binomial that represents a Binomial distribution"""


class Binomial:
    """class Binomial"""
    e = 2.7182818285
    pi = 3.1415926536

    def __init__(self, data=None, n=1, p=0.5):
        """class Binomial __init__"""
        if data is None:
            if n <= 0:
                raise ValueError("n must be a positive value")
            if not 0 < p < 1:
                raise ValueError("p must be greater than 0 and less than 1")
            self.n = n
            self.p = p
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            mean = sum(data) / len(data)
            stddev = sum(((x - mean) ** 2) for x in data) / len(data)
            self.p = 1 - (stddev / mean)
            self.n = round(mean / self.p)
            self.p = mean / self.n
