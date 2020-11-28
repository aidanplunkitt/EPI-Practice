from typing import List

from test_framework import generic_test, test_utils

# 15.3, O(n*n!) time, O(n^2) space?
def permutations(A: List[int]) -> List[List[int]]:
    def helper(elems, perms):
        if not elems:
            permutations.append(perms)
            return

        for i, a in enumerate(elems):
            helper(elems[:i] + elems[i+1:], perms + [a])

    permutations = []
    helper(A, [])
    return permutations


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('permutations.py', 'permutations.tsv',
                                       permutations,
                                       test_utils.unordered_compare))
