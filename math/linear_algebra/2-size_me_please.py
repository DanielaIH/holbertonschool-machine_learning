#!/usr/bin/env python3
import numpy as np
"""function that calculates the shape of a matrix"""


def matrix_shape(matrix):
    """shape of a matrix"""
    size = []
    while(type(matrix) is list):
        size.append(len(matrix))
        matrix = matrix[0]
    return size
