from typing import List

from bst_node import BstNode
from test_framework import generic_test, test_utils

# 14.3, O(h + k) time, O(h) space
def find_k_largest_in_bst(tree: BstNode, k: int) -> List[int]:
    def helper(tree):
        if tree and len(largest) < k:
            helper(tree.right)
            if len(largest) < k:
                largest.append(tree.data)
                helper(tree.left)

    largest = []
    helper(tree)
    return largest


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('k_largest_values_in_bst.py',
                                       'k_largest_values_in_bst.tsv',
                                       find_k_largest_in_bst,
                                       test_utils.unordered_compare))
