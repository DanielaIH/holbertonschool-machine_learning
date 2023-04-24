#!/usr/bin/env python3
import numpy as np
Normal = __import__('normal').Normal

np.random.seed(9)
m = np.random.uniform(-100., 100.)
s = np.random.uniform(5., 15.)
n = np.random.randint(100, 1000)
data = np.random.normal(m, s, n).tolist()
n = Normal()
print(n.mean, n.stddev)
n = Normal(data)
print(np.around(n.mean, 10), np.around(n.stddev, 10))
n = Normal(mean=m, stddev=s)
print(np.around(n.mean, 10), np.around(n.stddev, 10))