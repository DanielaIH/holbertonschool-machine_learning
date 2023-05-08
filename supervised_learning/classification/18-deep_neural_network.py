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

    @property
    def L(self):
        return self.__L

    @property
    def cache(self):
        return self.__cache

    @property
    def weights(self):
        return self.__weights
