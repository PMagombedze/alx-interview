#!/usr/bin/python3


def rotate_2d_matrix(matrix):
    """rotate 2d matrix"""
    matrix_size = len(matrix) - 1
    for i in range(len(matrix) // 2):
        for j in range(i, matrix_size - i):
            (
                matrix[i][j], matrix[~j][i], matrix[~i][~j], matrix[j][~i]
            ) = (
                matrix[~j][i], matrix[~i][~j], matrix[j][~i], matrix[i][j]
            )
    return matrix
