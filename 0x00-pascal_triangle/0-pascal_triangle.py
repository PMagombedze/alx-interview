"""
Pascal's tri
"""


def pascal_triangle(n):
    """
    returns list of ints representing pascal's
    triangle of n
    """
    if n <= 0:
        return []
    tri = [[1]]
    for x in range(1, n):
        pascal_row = [1]
        last_pascal_row = tri[-1]
        pascal_row += [sum(pair) for pair in zip(last_pascal_row, last_pascal_row[1:])]
        pascal_row.append(1)
        tri.append(pascal_row)
    return tri
