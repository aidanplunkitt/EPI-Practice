from typing import List

from test_framework import generic_test, test_utils

# 15.3, O(n*n!) time, O(n^2) space?
def permutations(A: List[int]) -> List[List[int]]:
    def helper(i):
        if i == len(A) - 1:
            permutations.append(A.copy())
            return

        for j in range(i, len(A)):
            A[i], A[j] = A[j], A[i]
            helper(i + 1)
            A[j], A[i] = A[i], A[j]

    permutations = []
    helper(0)
    return permutations


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('permutations.py', 'permutations.tsv',
                                       permutations,
                                       test_utils.unordered_compare))
