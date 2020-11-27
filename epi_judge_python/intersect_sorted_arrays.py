from typing import List

from test_framework import generic_test

# 13.1, O(min(A, B)) time, O(intersection(A, B)) space
def intersect_two_sorted_arrays(A: List[int], B: List[int]) -> List[int]:
    a = b = 0
    intersection = []
    while a < len(A) and b < len(B):
        if A[a] == B[b]:
            intersection.append(A[a])
            a, b = a+1, b+1
        elif A[a] < B[b]:
            a += 1
        else:
            b += 1

        while a > 0 and a < len(A) and A[a] == A[a-1]:
            a += 1
        while b > 0 and b < len(B) and B[b] == B[b-1]:
            b += 1

    return intersection 


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('intersect_sorted_arrays.py',
                                       'intersect_sorted_arrays.tsv',
                                       intersect_two_sorted_arrays))
