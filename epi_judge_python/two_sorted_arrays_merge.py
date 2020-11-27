from typing import List

from test_framework import generic_test

# 13.2, O(A + B) time and space
def merge_two_sorted_arrays(A: List[int], m: int, B: List[int],
                            n: int) -> None:
    a, b = m - 1, n - 1
    i = len(A) - 1
    while i >= 0:
        if a < 0:
            A[i] = B[b]
            b -= 1
        elif b < 0:
            i = -1 # return early, rest of A already in place
        elif A[a] >= B[b]:
            A[i] = A[a]
            a -= 1
        else:
            A[i] = B[b]
            b -= 1
        i -= 1


def merge_two_sorted_arrays_wrapper(A, m, B, n):
    merge_two_sorted_arrays(A, m, B, n)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('two_sorted_arrays_merge.py',
                                       'two_sorted_arrays_merge.tsv',
                                       merge_two_sorted_arrays_wrapper))
