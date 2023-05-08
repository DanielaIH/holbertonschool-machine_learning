#!/usr/bin/env python3
"""Deep Neural Network"""
import numpy as np


class DeepNeuralNetwork:
    """class NeuralNetwork that defines a deep neural
    network performing binary classification"""

    def __init__(self, nx, layers):
        """Initialize the Deep Neural Network"""
        if not isinstance(nx, int):
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")
        if not isinstance(layers, list) or len(layers) == 0:
            raise TypeError("layers must be a list of positive integers")

        self.nx = nx
        self.layers = layers
        self.__L = len(layers)
        self.__cache = {}
        self.__weights = {}

        """inicializar los pesos y sesgos de la red con He et aL"""
        for la in range(0, self.L):
            if layers[la] < 1:
                raise TypeError("layers must be a list of positive integers")
            if la == 0:
                l_prev = nx
            else:
                l_prev = layers[la - 1]
            self.weights['W' + str(la + 1)] = np.random.randn(
                layers[la], l_prev) * np.sqrt(2 / l_prev)
            self.weights['b' + str(la + 1)] = np.zeros((layers[la], 1))

    def forward_prop(self, X):
        """Calculates the forward propagation of the neural network"""
        self.__cache['A0'] = X
        for l in range(1, self.__L + 1):
            A_prev = self.__cache['A' + str(l - 1)]
            W = self.__weights['W' + str(l)]
            b = self.__weights['b' + str(l)]
            Z = np.dot(W, A_prev) + b
            A = 1 / (1 + np.exp(-Z))
            self.__cache['A' + str(l)] = A
        return A, self.__cache

    def cost(self, Y, A):
        """Calculates the cost of the model using logistic regression"""
        m = Y.shape[1]
        cost = - np.sum(Y * np.log(A) + (1-Y) * np.log(1.0000001 - A)) / m
        return cost

    def evaluate(self, X, Y):
        """Evaluates the neural network's predictions"""
        A = self.forward_prop(X)[0]
        cost = self.cost(Y, A)
        prediction = np.where(A >= 0.5, 1, 0)
        return prediction, cost

    def gradient_descent(self, Y, cache, alpha=0.05):
        """Calculates one pass of gradient descent on the neural network"""
        m = Y.shape[1]
        dz = cache['A' + str(self.__L)] - Y
        for l in range(self.__L, 0, -1):
            A_prev = cache['A' + str(l-1)]
            dw = (1/m) * np.matmul(dz, A_prev.T)
            db = (1/m) * np.sum(dz, axis=1, keepdims=True)
            dz = (np.matmul(self.__weights['W'+str(l)].T, dz) *
                  (A_prev * (1 - A_prev)))
            self.__weights['W'+str(l)] -= alpha * dw
            self.__weights['b'+str(l)] -= alpha * db

    def train(self, X, Y, iterations=5000, alpha=0.05, verbose=True,
              graph=True, step=100):
        """ Trains the deep neural network """
        if type(iterations) != int:
            raise TypeError("iterations must be an integer")
        if iterations <= 0:
            raise ValueError("iterations must be a positive integer")
        if type(alpha) != float:
            raise TypeError("alpha must be a float")
        if alpha <= 0:
            raise ValueError("alpha must be positive")
        if verbose or graph:
            if type(step) != int:
                raise TypeError("step must be an integer")
            if step <= 0 or step >= iterations:
                raise ValueError("step must be positive and <= iterations")
        costs = []
        for i in range(iterations + 1):
            if verbose and i % 100 == 0:
                _, cost = self.evaluate(X, Y)
                costs.append(cost)
                print("Cost after {} iterations: {}".format(i, cost))
            if i != iterations:
                _, cache = self.forward_prop(X)
                self.gradient_descent(Y, cache, alpha)

        if graph:
            plt.plot(np.arange(0, iterations, step), costs, 'b-')
            plt.xlabel('iteration')
            plt.ylabel('cost')
            plt.title('Training Cost')
            plt.show()

        return self.evaluate(X, Y)

    @property
    def L(self):
        return self.__L

    @property
    def cache(self):
        return self.__cache

    @property
    def weights(self):
        return self.__weights
