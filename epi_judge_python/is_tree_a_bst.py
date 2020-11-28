from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

# 14.1, O(n) time, O(height) callstack space (height == n in worst case)
def is_binary_tree_bst(tree: BinaryTreeNode) -> bool:
    def helper(tree, lower_limit=float("-inf"), upper_limit=float("inf")):
        if not tree: 
            return True

        if not lower_limit <= tree.data <= upper_limit: 
            return False

        return helper(tree.left, lower_limit, tree.data) and helper(tree.right, tree.data, upper_limit)
        
    return helper(tree)

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_a_bst.py', 'is_tree_a_bst.tsv',
                                       is_binary_tree_bst))
