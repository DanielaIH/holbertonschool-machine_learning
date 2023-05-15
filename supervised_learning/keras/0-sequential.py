#!/usr/bin/env python3
"""supervised_learning keras"""
import tensorflow.keras as K


def build_model(nx, layers, activations, lambtha, keep_prob):
    """function that builds a neural network with the Keras library"""
    if len(layers) != len(activations):
        raise ValueError("Number of layers and activations must be the same")

    k_reg = K.regularizers.l2(lambtha)

    model = K.Sequential()
    model.add(K.layers.Dense(layers[0], activation=activations[0],
                             kernel_regularizer=k_reg,
                             input_shape=(nx,)))

    for i in range(1, len(layers)):
        model.add(K.layers.Dropout(1 - keep_prob))
        model.add(K.layers.Dense(layers[i], activation=activations[i],
                                 kernel_regularizer=k_reg))

    return model
