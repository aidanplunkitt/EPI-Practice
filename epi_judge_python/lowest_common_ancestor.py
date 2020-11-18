import functools
from typing import Optional

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node, strip_parent_link
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def lca(tree: BinaryTreeNode, node0: BinaryTreeNode,
        node1: BinaryTreeNode) -> Optional[BinaryTreeNode]:
    def find_path_to_node(tree, node):
        if tree is node:
            return True, [tree]

        if tree.left:
            found, path = find_path_to_node(tree.left, node)
            if found:
                return True, path + [tree]

        if tree.right:
            found, path = find_path_to_node(tree.right, node)
            if found:
                return True, path + [tree]
        
        return False, None
                
    _, path0 = find_path_to_node(tree, node0)
    _, path1 = find_path_to_node(tree, node1)

    path0.reverse()
    path1.reverse()

    for i in range(min(len(path0), len(path1))):
        if path0[i] != path1[i]: return path0[i-1]

    return path0[i]


@enable_executor_hook
def lca_wrapper(executor, tree, key1, key2):
    strip_parent_link(tree)
    result = executor.run(
        functools.partial(lca, tree, must_find_node(tree, key1),
                          must_find_node(tree, key2)))

    if result is None:
        raise TestFailure('Result can\'t be None')
    return result.data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('lowest_common_ancestor.py',
                                       'lowest_common_ancestor.tsv',
                                       lca_wrapper))
