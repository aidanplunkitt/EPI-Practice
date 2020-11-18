from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def is_symmetric(tree: BinaryTreeNode) -> bool:
    def nodes_symmetric(left, right):
        if not (left or right): return True
        if not (left and right): return False

        to_visit_left, to_visit_right = [left], [right]

        while to_visit_left and to_visit_right:
            l, r = to_visit_left.pop(), to_visit_right.pop()
            if l.data != r.data: return False

            if l.right: to_visit_left.append(l.right)
            if l.left: to_visit_left.append(l.left)

            if r.left: to_visit_right.append(r.left)
            if r.right: to_visit_right.append(r.right)

        return False if to_visit_left or to_visit_right else True

    if not tree: return True
    return nodes_symmetric(tree.left, tree.right)

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_symmetric.py',
                                       'is_tree_symmetric.tsv', is_symmetric))
