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
        self.L = len(layers)
        self.cache = {}
        self.weights = {}

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
