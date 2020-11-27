from typing import List

from test_framework import generic_test

import bisect

# 13.1, O(A log B) time, O(intersection(A, B)) space
def intersect_two_sorted_arrays(A: List[int], B: List[int]) -> List[int]:
    def in_array(arr, elem):
        i = bisect.bisect_left(arr, elem)
        return i < len(arr) and elem == arr[i]

    return [a for i, a in enumerate(A) if (i == 0 or a != A[i-1]) and in_array(B, a)] 


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('intersect_sorted_arrays.py',
                                       'intersect_sorted_arrays.tsv',
                                       intersect_two_sorted_arrays))
