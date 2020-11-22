from typing import List

from test_framework import generic_test

import random

# The numbering starts from one, i.e., if A = [3, 1, -1, 2]
# find_kth_largest(1, A) returns 3, find_kth_largest(2, A) returns 2,
# find_kth_largest(3, A) returns 1, and find_kth_largest(4, A) returns -1.
# 11.8, O(n) time, O(1) space
def find_kth_largest(k: int, A: List[int]) -> int:
    def sort_around_pivot(left, right, pivot):
        val = A[pivot]
        A[pivot], A[right] = A[right], A[pivot]
        old = right
        while left <= right:
            if A[right] > val:
                A[left], A[right] = A[right], A[left]
                left += 1
            else:
                right -= 1

        A[old], A[left] = A[left], A[old]
        return left

    left, right = 0, len(A) - 1
    while left <= right:
        pivot = sort_around_pivot(left, right, random.randint(left, right))
        if pivot == k - 1:
            return A[pivot]
        elif pivot > k - 1:
            right = pivot - 1
        else: 
            left = pivot + 1

    # shouldn't get here


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('kth_largest_in_array.py',
                                       'kth_largest_in_array.tsv',
                                       find_kth_largest))
