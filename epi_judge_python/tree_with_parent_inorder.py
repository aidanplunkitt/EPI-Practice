from typing import List

from binary_tree_with_parent_prototype import BinaryTreeNode
from test_framework import generic_test


def inorder_traversal(tree: BinaryTreeNode) -> List[int]:
    traversal = []
    node = tree
    while node:
        # walk down the left side to find first node to print (in-order first is leftmost node)
        while node.left:
            node = node.left
        traversal.append(node.data)

        # if not a leaf
        if node.right:
            # remove this node by moving parent and child pointers to each other
            if node.parent:
                node.parent.left = node.right
                node.right.parent = node.parent
            # but if we're at the root node, instead just make right subtree the new root
            else:
                tree = node.right
                tree.parent = None
        # if a leaf
        else:
            # remove this node by removing the reference to it
            if node.parent:
                node.parent.left = None
            # if it's the root node, we're done
            else:
                tree = None

        node = tree

    return traversal


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_with_parent_inorder.py',
                                       'tree_with_parent_inorder.tsv',
                                       inorder_traversal))
