#!/usr/bin/env python3
"""function that adds two matrices element-wise:"""


def add_matrices2D(mat1, mat2):
    """add matrices2D"""
    new_matrix = []
    if (len(mat1[0]) == len(mat2[0])):
        for i in range(len(mat1)):
            new_array = []
            for j in range(len(mat1[0])):
                new_array.append(mat1[i][j]+mat2[i][j])
            new_matrix.append(new_array)
        return(new_matrix)
    return None
