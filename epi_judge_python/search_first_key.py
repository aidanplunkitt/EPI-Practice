from typing import List

from test_framework import generic_test

import bisect

# 11.1, O(log n) time, O(1) space
def search_first_of_k(A: List[int], k: int) -> int:
    index = bisect.bisect_left(A, k)
    if index == len(A) or (A[index] != k):
        index = -1
    return index


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_first_key.py',
                                       'search_first_key.tsv',
                                       search_first_of_k))
