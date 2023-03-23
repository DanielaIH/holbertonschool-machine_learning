#!/usr/bin/env python3
"""function that that adds two arrays element-wise"""


def add_arrays(arr1, arr2):
    """add arrays"""
    new_array = []
    if (len(arr1) == len(arr2)):
        for i in range(len(arr1)):
            new_array.append(arr1[i]+arr2[i])
        return new_array
    return None
