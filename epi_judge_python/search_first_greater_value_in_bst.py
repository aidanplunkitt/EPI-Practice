from typing import Optional

from bst_node import BstNode
from test_framework import generic_test

# 14.2, O(h) time (O(log n) avg, O(n) worst-case), O(1) space
def find_first_greater_than_k(tree: BstNode, k: int) -> Optional[BstNode]:
    last = BstNode(-1)
    while tree:
        if tree.data > k:
            last, tree = tree, tree.left
        else:
            tree = tree.right
    return last


def find_first_greater_than_k_wrapper(tree, k):
    result = find_first_greater_than_k(tree, k)
    return result.data if result else -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'search_first_greater_value_in_bst.py',
            'search_first_greater_value_in_bst.tsv',
            find_first_greater_than_k_wrapper))
