#!/usr/bin/python3

"""
module to rotate a 2 by 2 matrix
"""


def rotate_2d_matrix(matrix):
    """
    funtion to rotate a two by two matrix
    """
    n = len(matrix)

    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(n):
        matrix[i].reverse()
