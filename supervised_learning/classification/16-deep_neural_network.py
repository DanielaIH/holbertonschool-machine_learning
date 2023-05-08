#!/usr/bin/env python3
"""Deep Neural Network"""
import numpy as np


class DeepNeuralNetwork:
    """class NeuralNetwork that defines a deep neural
    network performing binary classification"""

    def __init__(self, nx, layers):
        if not isinstance(nx, int):
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")
        if not isinstance(layers, list) or len(layers) == 0:
            raise TypeError("layers must be a list of positive integers")
        if not all(isinstance(i, int) and i > 0 for i in layers):
            raise TypeError("layers must be a list of positive integers")

        self.nx = nx
        self.layers = layers
        self.L = len(layers)
        self.cache = {}
        self.weights = {}

        """inicializar los pesos y sesgos de la red con He et aL"""
        for l in range(1, self.L+1):
            self.weights["W" + str(l)] = (np.random.randn(layers[l-1], nx)
                                          * np.sqrt(2/nx))
            self.weights["b" + str(l)] = np.zeros((layers[l-1], 1))
