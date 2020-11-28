from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

# 14.1, O(n) time, O(1) space
def is_binary_tree_bst(tree: BinaryTreeNode) -> bool:
    def next_node(node):
        if node.right:
            node = node.right
            while node.left:
                node = node.left
            return node

        while node.parent and node.parent.right is node:
            node = node.parent
        return node.parent

    if not tree: return True

    # go to smallest node
    while tree.left:
        tree = tree.left

    # walk tree checking that it's sorted
    while True:
        last_val, tree = tree.data, next_node(tree)
        if not tree: break
        if tree.data < last_val: return False

    return True

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_a_bst.py', 'is_tree_a_bst.tsv',
                                       is_binary_tree_bst))
