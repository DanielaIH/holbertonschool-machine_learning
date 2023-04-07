#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
np.random.seed(5)
fruit = np.random.randint(0, 20, (4,3))

x = np.arange(fruit.shape[0])
x_labels = ["Farrah", "Fred", "Felicia"]
fruits = ['apples', 'bananas', 'oranges', 'peaches']
colors = ['r', 'yellow', '#ff8000', '#ffe5b4']

fig, ax=plt.subplots()

for i in range(len(fruit)):
    bottom=np.sum(fruit[0:i], axis=0)
    ax.bar(x_labels, fruit[i], width=0.5, bottom=bottom, label=fruits[i], color=colors[i])
plt.ylim(0, 80)
plt.ylabel('Quantity of Fruit')
plt.title('Number of Fruit per Person')
plt.legend()