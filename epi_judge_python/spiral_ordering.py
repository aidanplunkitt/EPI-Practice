from typing import List

from test_framework import generic_test


def matrix_in_spiral_order(square_matrix: List[List[int]]) -> List[int]:
    n = len(square_matrix)
    if n == 1: return square_matrix[0]

    ordering = []
    for i in range(n // 2):
        # top
        ordering += square_matrix[i][i:n-i]
        # right
        ordering += [row[n-i-1] for row in square_matrix[i+1:n-i-1]]
        # bottom
        ordering += reversed(square_matrix[n-i-1][i:n])
        # left
        ordering += reversed([row[i] for row in square_matrix[i+1:n+i-1]])

    if n % 2 != 0:
        ordering += square_matrix[n//2][n//2]

    return ordering

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('spiral_ordering.py',
                                       'spiral_ordering.tsv',
                                       matrix_in_spiral_order))
