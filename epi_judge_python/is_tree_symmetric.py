from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def is_symmetric(tree: BinaryTreeNode) -> bool:
    def nodes_symmetric(left, right):
        if not (left or right): return True
        if not (left and right): return False

        return left.data == right.data and \
                nodes_symmetric(left.left, right.right) and \
                nodes_symmetric(left.right, right.left)

    if not tree: return True
    return nodes_symmetric(tree.left, tree.right)

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_symmetric.py',
                                       'is_tree_symmetric.tsv', is_symmetric))
