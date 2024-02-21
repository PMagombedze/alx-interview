#!/usr/bin/python3


def rotate_2d_matrix(matrix):
    """
    Rotates a 2D matrix 90 degrees clockwise.
    """
    n = len(matrix)
    for x in range(n // 2):
        a, b = x, n - 1 - x
        for i in range(a, b):
            start = matrix[x][i]
            matrix[x][i] = matrix[n - 1 - i][x]
            matrix[n - 1 - i][x] = matrix[n - 1 - x][n - 1 - i]
            matrix[n - 1 - x][n - 1 - i] = matrix[i][n - 1 - x]
            matrix[i][n - 1 - x] = start
