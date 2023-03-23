#!/usr/bin/env python3
"""function that returns the transpose of a 2D matrix, matrix"""


def matrix_transpose(matrix):
    """transpose of a matrix"""
    new_matrix = []
    for i in range(len(matrix[0])):
        new_array = []
        for j in range(len(matrix)):
            new_array.append(matrix[j][i])
        new_matrix.append(new_array)
    return new_matrix
