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
        for la in range(1, self.L+1):
            if layers[la - 1] < 1:
                raise TypeError("layers must be a list of positive integers")
            if la == 1:
                l_prev = nx
            else:
                l_prev = layers[la - 1]
            self.weights["W"+str(la)] = (np.random.randn(layers[la-1], l_prev)
                                         * np.sqrt(2/nx))
            self.weights["b"+str(la)] = np.zeros((layers[la-1], 1))
            nx = layers[la - 1]
