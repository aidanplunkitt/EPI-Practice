from typing import List

from test_framework import generic_test

import bisect

# 11.1, O(log n) time, O(1) space
def search_first_of_k(A: List[int], k: int) -> int:
    left, right, result = 0, len(A) - 1, -1
    while left <= right:
        mid = (left + right) // 2
        if A[mid] == k:
            result = mid
            right = mid - 1
        elif A[mid] > k:
            right = mid - 1
        else: # A[mid] < k
            left = mid + 1

    return result

# Pythonic solution:
def pythonic_search_first_of_k(A: List[int], k: int) -> int:
    i = bisect.bisect_left(A, k)
    return i if i < len(A) and A[i] == k else -1



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_first_key.py',
                                       'search_first_key.tsv',
                                       search_first_of_k))
