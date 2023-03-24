#!/usr/bin/env python3
"""function that concatenates two matrices"""

import numpy as np


def np_cat(mat1, mat2, axis=0):
    """concatenates two matrices"""
    return(np.append(mat1, mat2, axis=axis))
