from typing import List

from binary_tree_with_parent_prototype import BinaryTreeNode
from test_framework import generic_test


def inorder_traversal(tree: BinaryTreeNode) -> List[int]:
    def find_successor(node):
        if node.right:
            node = node.right
            while node.left:
                node = node.left
            return node

        while node.parent and node.parent.right is node:
            node = node.parent

        return node.parent

    # set tree to first elem in traversal
    while tree.left:
        tree = tree.left

    trav = []
    while True:
        trav.append(tree.data)
        tree = find_successor(tree)
        if not tree: break

    return trav


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_with_parent_inorder.py',
                                       'tree_with_parent_inorder.tsv',
                                       inorder_traversal))
