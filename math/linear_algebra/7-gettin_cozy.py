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
            except:
                pass
            try:
                if (len(mat2[i]) == 0):
                    return None
            except:
                pass
            new_matrix.append(mat2[i])

        return(new_matrix)
    except IndexError:
        return None


m1 = [[1]]
m2 = [[2]]
m = cat_matrices2D(m1, m2)
if type(m) is not list or m is m1 or m is m2 or not len(m) or type(m[0]) is not list:
    print("Not a new matrix")

print(m)
m1 = [[4, -7, 56, 2], [5, 106, 7, 2]]
m2 = [[2, -6, 3, 23], [0, -6, 3, 42], [73, 8, 2, 99]]
m = cat_matrices2D(m1, m2)
if type(m) is not list or m is m1 or m is m2 or not len(m) or type(m[0]) is not list:
    print("Not a new matrix")

print(m)
m1 = [[484, 247, -556], [554, 16, 75], [5, 88, 23]]
m2 = [[233, -644, 325], [406, -16, 33]]
m = cat_matrices2D(m1, m2, axis=0)
if type(m) is not list or m is m1 or m is m2 or not len(m) or type(m[0]) is not list:
    print("Not a new matrix")

print(m)
m1 = [[-54, -87, 56, -92, 81], [54, 16, -72, 42, 901]]
m2 = [[12, 63], [-10, 69]]
m = cat_matrices2D(m1, m2, axis=1)
if type(m) is not list or m is m1 or m is m2 or not len(m) or type(m[0]) is not list:
    print("Not a new matrix")

print(m)

m1 = [[51, 24, 73], [93, 45, 77]]
m2 = [[], [], []]
m = cat_matrices2D(m1, m2)
print(m)
m2 = [[51, 24, 73], [93, 45, 77]]
m1 = [[], [], []]
m = cat_matrices2D(m1, m2, axis=0)
print(m)
m1 = [[75, 23, 58], [32, 5, 67], [34, 65, 22]]
m2 = [[], [], []]
m = cat_matrices2D(m1, m2, axis=1)
if type(m) is not list or m is m1 or m is m2 or not len(m) or type(m[0]) is not list:
    print("Not a new matrix")

print(m)