from typing import List

from bst_node import BstNode
from test_framework import generic_test, test_utils

# 14.3, O(n) time, O(1) space
def find_k_largest_in_bst(tree: BstNode, k: int) -> List[int]:
    def get_next(node):
        if node.left:
            node = node.left
            while node.right:
                node = node.right
            return node

        while node.parent and node.parent.left is node:
            node = node.parent
        return node.parent

    if not tree: return []

    # start at max
    while tree.right:
        tree = tree.right

    # reverse in-order walk
    largest = []
    for _ in range(k):
        largest.append(tree.data)
        tree = get_next(tree)
        if not tree: break

    return largest


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('k_largest_values_in_bst.py',
                                       'k_largest_values_in_bst.tsv',
                                       find_k_largest_in_bst,
                                       test_utils.unordered_compare))
