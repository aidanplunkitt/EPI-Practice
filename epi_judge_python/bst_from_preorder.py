from typing import List, Optional

from bst_node import BstNode
from test_framework import generic_test

# 14.5, O(n^2) time, O(n) space
def rebuild_bst_from_preorder(preorder_sequence: List[int]
                              ) -> Optional[BstNode]:
    if not preorder_sequence: return None
    root = BstNode(preorder_sequence[0])
    for i in range(1, len(preorder_sequence)):
        node = prev_node = root
        val = preorder_sequence[i]
        left = val < node.data
        while node:
            prev_node = node
            if val < node.data:
                node, left = node.left, True
            else:
                node, left = node.right, False
        new_node = BstNode(val)
        if left:
            prev_node.left  = new_node
        else:
            prev_node.right = new_node

    return root



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('bst_from_preorder.py',
                                       'bst_from_preorder.tsv',
                                       rebuild_bst_from_preorder))
