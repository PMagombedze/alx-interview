#!/usr/bin/python3


def rotate_2d_matrix(matrix):
    """Rotate 2D matrix"""
    matrix_size = len(matrix)
    for i in range(matrix_size // 2):
        for j in range(i, matrix_size - i - 1):
            matrix[i][j], matrix[j][matrix_size - i - 1], matrix[matrix_size - i - 1][matrix_size - j - 1], matrix[matrix_size - j - 1][i] = \
                matrix[matrix_size - j - 1][i], matrix[i][j], matrix[j][matrix_size - i - 1], matrix[matrix_size - i - 1][matrix_size - j - 1]
    return matrix
