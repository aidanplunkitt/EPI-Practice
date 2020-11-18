from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def is_balanced_binary_tree(tree: BinaryTreeNode) -> bool:
    def get_height(subtree):
        left, isBalanced = get_height(subtree.left) if subtree.left else (0, True)
        if not isBalanced: return 0, False

        right, isBalanced = get_height(subtree.right) if subtree.right else (0, True)
        if not isBalanced: return 0, False

        if abs(left - right) > 1:
            return 0, False

        return max(left + 1, right + 1), True

    if not tree: return True
    _, isBalanced = get_height(tree)
    return isBalanced


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_balanced.py',
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
