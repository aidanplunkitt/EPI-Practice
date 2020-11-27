from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

# 14.1, O(n) time, O(height) callstack space (height == n in worst case) + O(n) space to cache the min/maxes at each node
def is_binary_tree_bst(tree: BinaryTreeNode) -> bool:
    def helper(tree):
        is_bst = True
        maxval = minval = tree.data
        if tree.left:
            is_bst, leftmin, leftmax = helper(tree.left)
            if not is_bst or leftmax > tree.data:
                return False, None, None
            minval, maxval = min(minval, leftmin), max(maxval, leftmax)

        if tree.right:
            is_bst, rightmin, rightmax = helper(tree.right)
            if not is_bst or rightmin < tree.data:
                return False, None, None
            minval, maxval = min(minval, rightmin), max(maxval, rightmax)

        return is_bst, minval, maxval

    is_bst, _, _ = helper(tree)
    return is_bst


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_a_bst.py', 'is_tree_a_bst.tsv',
                                       is_binary_tree_bst))
