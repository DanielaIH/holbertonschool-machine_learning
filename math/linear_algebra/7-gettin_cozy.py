#!/usr/bin/env python3
"""function that concatenates two matrices along a specific axis"""


def cat_matrices2D(mat1, mat2, axis=0):
    """concatenates two matrices"""
    new_matrix = []
    try:
        if (len(mat1[0]) == len(mat2[0])):
            if (axis):
                new_matrix = [row[:] for row in mat1]
                for i in range(len(new_matrix[0])):
                    new_matrix[i].append(mat2[i][0])
                return(new_matrix)
            new_matrix = [row[:] for row in mat1]
            for i in range(len(mat2)):
                new_matrix.append(mat2[i])
            return(new_matrix)
    except IndexError:
        return None
