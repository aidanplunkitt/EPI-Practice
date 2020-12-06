from test_framework import generic_test

# 16.3, O(nm) time and space
def number_of_ways(n: int, m: int) -> int:
    matrix = [[0] * m for _ in range(n)]

    for i in range(m):
        matrix[0][i] = 1
    for i in range(n):
        matrix[i][0] = 1

    for i in range(1, n):
        for j in range(1, m):
            matrix[i][j] = matrix[i][j-1] + matrix[i-1][j]

    return matrix[-1][-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('number_of_traversals_matrix.py',
                                       'number_of_traversals_matrix.tsv',
                                       number_of_ways))
