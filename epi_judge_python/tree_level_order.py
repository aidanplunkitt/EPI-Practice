from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
import collections


def binary_tree_depth_order(tree: BinaryTreeNode) -> List[List[int]]:
    ans, q = [], [tree]

    while q:
        ans.append([n.data for n in q])
        q = [child for node in q for child in (node.left, node.right) if child]

    return ans


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_level_order.py',
                                       'tree_level_order.tsv',
                                       binary_tree_depth_order))
