from typing import List

from test_framework import generic_test

# 17.4, O(n^2) time, O(n) space
def has_three_sum(A: List[int], t: int) -> bool:
    nums = set()
    for a in A:
        nums.add(t - a)

    for i in range(len(A)):
        for j in range(i, len(A)):
            if (A[i] + A[j]) in nums:
                return True
            
    return False


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('three_sum.py', 'three_sum.tsv',
                                       has_three_sum))
