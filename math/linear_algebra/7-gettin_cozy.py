#!/usr/bin/env python3
"""function that concatenates two matrices along a specific axis"""


def cat_matrices2D(mat1, mat2, axis=0):
    """concatenates two matrices"""
    new_matrix = []
    try:
        if (axis):
            new_matrix = [row[:] for row in mat1]
            for i in range(len(mat1)):
                new_matrix[i] += mat2[i]
            return(new_matrix)
        new_matrix = [row[:] for row in mat1]
        for i in range(len(mat2)):
            try:
                if (len(mat1[i]) == 0):
                    return None
            except IndexError:
                pass
            try:
                if (len(mat2[i]) == 0):
                    return None
            except IndexError:
                pass
            new_matrix.append(mat2[i])

        return(new_matrix)
    except IndexError:
        return None
