#!/usr/bin/env python3
import numpy as np
Normal = __import__('normal').Normal

np.random.seed(12)
m = np.random.uniform(-100., 100.)
s = np.random.uniform(5., 15.)
n = np.random.randint(100, 1000)
data = np.random.normal(m, s, n).tolist()
n = Normal(data)
x = np.random.randint(int(m - 3 * s), int(m + 3 * s))
print(np.around(n.cdf(x), 10))
x = np.random.uniform(m - 3 * s, m + 3 * s)
print(np.around(n.cdf(x), 10))