#!/usr/bin/python3


def rotate_2d_matrix(matrix):
    """
    rotate 2d matrix clockwise

    Args:
        matrix (List[List[int]]): The input matrix.

    Returns:
        None: The matrix is modified in-place.
    """
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for x in matrix:
        x.reverse()
