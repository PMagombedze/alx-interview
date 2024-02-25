#!/usr/bin/python3
"""
2d matrix rotation
"""

def transpose(matrix):
    """matrix transpose"""
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

def rotate_2d_matrix(matrix):
    """
    rotate 2d matrix clockwise

    Args:
        matrix (List[List[int]]): The input matrix.

    Returns:
        None: The matrix is modified in-place.
    """
    transpose(matrix)
    for x in matrix:
        x.reverse()
