from typing import List

from test_framework import generic_test

# 17.4, O(n^2) time, O(1) space
def has_three_sum(A: List[int], t: int) -> bool:
    def has_two_sum(A, t):
        i, j = 0, len(A) - 1
        while i <= j:
            n = A[i] + A[j]
            if n < t:
                i += 1
            elif n > t:
                j -= 1
            else:
                return True
        return False

    A.sort()
    return any(has_two_sum(A, t-a) for a in A)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('three_sum.py', 'three_sum.tsv',
                                       has_three_sum))
