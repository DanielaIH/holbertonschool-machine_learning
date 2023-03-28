#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

y0 = np.arange(0, 11) ** 3

mean = [69, 0]
cov = [[15, 8], [8, 15]]
np.random.seed(5)
x1, y1 = np.random.multivariate_normal(mean, cov, 2000).T
y1 += 180

x2 = np.arange(0, 28651, 5730)
r2 = np.log(0.5)
t2 = 5730
y2 = np.exp((r2 / t2) * x2)

x3 = np.arange(0, 21000, 1000)
r3 = np.log(0.5)
t31 = 5730
t32 = 1600
y31 = np.exp((r3 / t31) * x3)
y32 = np.exp((r3 / t32) * x3)

np.random.seed(5)
student_grades = np.random.normal(68, 15, 50)

fig = plt.figure(figsize=(8, 6))
fig.suptitle("All in One")

plt.subplot(321)
plt.xlim(0, 10)
plt.plot(y0, 'r')

plt.subplot(322)
plt.scatter(x1, y1, s=5, c='MAGENTA')
plt.xlabel('Height (in)', size="x-small")
plt.ylabel('Weight (lbs)', size="x-small")
plt.title("Men's Height vs Weight", size="x-small")

plt.subplot(323)
plt.plot(x2, y2)
plt.xlabel("Time (years)", size="x-small")
plt.ylabel("Fraction Remaining", size="x-small")
plt.title("Exponential Decay of C-14", size="x-small")
plt.yscale("log")
plt.xlim(0, 28650)

plt.subplot(324)
plt.plot(x3, y31, '--r', x3, y32, 'g')
plt.xlabel("Time (years)", size="x-small")
plt.ylabel("Fraction Remaining", size="x-small")
plt.title("Exponential Decay of Radioactive Elements", size="x-small")
plt.xlim(0, 20000)
plt.ylim(0, 1)
plt.legend(['C-14', 'Ra-226'])

plt.subplot(313)
intervalo = range(0, 109, 10)
plt.hist(student_grades, bins=intervalo, edgecolor='black')
plt.xlabel('Grades', size="x-small")
plt.ylabel('Number of Students', size="x-small")
plt.title('Project A', size="x-small")
plt.xlim(0, 100)
plt.ylim(0, 30)
plt.xticks(intervalo)

# Adjust the padding between and around subplots.
plt.tight_layout()
