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
    
    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        last_row = triangle[i - 1]
        for j in range(1, i):
            row.append(last_row[j - 1] + last_row[j])
        row.append(1)
        triangle.append(row)
    
    return triangle
