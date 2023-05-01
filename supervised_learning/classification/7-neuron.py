#!/usr/bin/env python3
"""1. Neuron"""
import numpy as np
import matplotlib.pyplot as plt


class Neuron:
    """class Neuron that defines a single
    neuron performing binary classification"""
    def __init__(self, nx):
        """init function"""
        if not isinstance(nx, int):
            raise TypeError("nx must be an integer")
        if (nx < 1):
            raise ValueError("nx must be a positive integer")
        self.__W = np.random.normal(size=(1, nx))
        self.__b = 0
        self.__A = 0

    @property
    def W(self):
        return self.__W

    @property
    def b(self):
        return self.__b

    @property
    def A(self):
        return self.__A

    def forward_prop(self, X):
        """Calculates the forward propagation of the neuron"""
        Z = np.matmul(self.__W, X) + self.__b
        self.__A = 1 / (1 + np.exp(-Z))

        return self.__A

    def cost(self, Y, A):
        """Calculates the cost of the model using logistic regression"""
        m = Y.shape[1]
        cost = - np.sum(Y * np.log(A) + (1-Y) * np.log(1.0000001 - A)) / m
        return cost

    def evaluate(self, X, Y):
        """Evaluates the neuron's predictions"""
        A = self.forward_prop(X)
        cost = self.cost(Y, A)
        prediction = np.where(A >= 0.5, 1, 0)
        return prediction, cost

    def gradient_descent(self, X, Y, A, alpha=0.05):
        """Calculates one pass of gradient descent on the neuron"""
        m = Y.shape[1]
        dz = A - Y
        dw = (1 / m) * np.matmul(X, dz.T)
        db = (1 / m) * np.sum(dz)
        self.__W = self.__W - alpha * dw.T
        self.__b = self.__b - alpha * db

    def train(self, X, Y, iterations=5000, alpha=0.05, verbose=True,
              graph=True, step=100):
        """Trains the neuron"""
        if not isinstance(iterations, int):
            raise TypeError("iterations must be an integer")
        if iterations <= 0:
            raise ValueError("iterations must be a positive integer")
        if not isinstance(alpha, float):
            raise TypeError("alpha must be a float")
        if alpha <= 0:
            raise ValueError("alpha must be positive")
        if not isinstance(step, int):
            raise TypeError("step must be an integer")
        if step <= 0 or step > iterations:
            raise ValueError("step must be positive and <= iterations")
        costs = []
        iters = []
        for i in range(iterations + 1):
            A = self.forward_prop(X)
            cost = self.cost(Y, A)
            if i % step == 0 or i == 0 or i == iterations:
                costs.append(cost)
                iters.append(i)
                if verbose:
                    print("Cost after {} iterations: {}".format(i, cost))
            self.gradient_descent(X, Y, A, alpha)
        if graph:
            plt.plot(iters, costs)
            plt.xlabel("iteration")
            plt.ylabel("cost")
            plt.title("Training Cost")
            plt.show()
        return self.evaluate(X, Y)
