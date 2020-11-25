from typing import List

from test_framework import generic_test

# 11.3, O(log n) time, O(1) space
def search_smallest(A: List[int]) -> int:
    left, right = 0, len(A) - 1
    while A[left] > A[right]:
        mid = (left + right) // 2
        if A[mid] < A[left]:
            right = mid
        else:
            left = mid + 1

    return left


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_shifted_sorted_array.py',
                                       'search_shifted_sorted_array.tsv',
                                       search_smallest))
