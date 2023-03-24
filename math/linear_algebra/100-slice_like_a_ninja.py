#!/usr/bin/env python3
"""function that slices a matrix along specific axes"""


def np_slice(matrix, axes={}):
    """slices a matrix"""
    new_matrix = (max(axes) + 1) * [slice(None)]
    for k, v in axes.items():
        new_matrix[k] = slice(*v)
    result = matrix[tuple(new_matrix)]
    return result
