#!/usr/bin/env python3
"""supervised_learning keras"""
import tensorflow.keras as K


def build_model(nx, layers, activations, lambtha, keep_prob):
    """function that builds a neural network with the Keras library"""
    if len(layers) != len(activations):
        raise ValueError("Number of layers and activations must be the same")

    k_reg = K.regularizers.l2(lambtha)
    inputs = K.Input(shape=(nx,))
    x = inputs

    for i in range(len(layers)):
        x = K.layers.Dense(layers[i], activation=activations[i],
                           kernel_regularizer=k_reg)(x)
        if (i < len(layers) - 1):
            x = K.layers.Dropout(1 - keep_prob)(x)

    model = K.Model(inputs=inputs, outputs=x)
    return model
