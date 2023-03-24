#!/usr/bin/env python3
import numpy as np
"""function that concatenates two matrices"""


def np_cat(mat1, mat2, axis=0):
    """concatenates two matrices"""
    return(np.append(mat1, mat2, axis=axis))
