#!/usr/bin/env python3
"""function  that performs matrix multiplication"""


def mat_mul(mat1, mat2):
    """performs matrix multiplication"""
    try:
        if (len(mat1[0]) != len(mat2)):
            return None
    except IndexError:
        return None

    new_matrix = []
    for i in range(len(mat1)):
        new_array = []
        for j in range(len(mat2[0])):
            cc = 0
            for k in range(len(mat1[0])):
                cc += mat1[i][k] * mat2[k][j]
            new_array.append(cc)
        new_matrix.append(new_array)
    return (new_matrix)
