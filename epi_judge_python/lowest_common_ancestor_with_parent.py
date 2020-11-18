import functools
from typing import Optional

from binary_tree_with_parent_prototype import BinaryTreeNode
from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def lca(node0: BinaryTreeNode,
        node1: BinaryTreeNode) -> Optional[BinaryTreeNode]:
    path0, path1 = [], []

    n = node0
    while True:
        path0.append(n)
        if not n.parent: break
        n = n.parent
    n = node1
    while True:
        path1.append(n)
        if not n.parent: break
        n = n.parent

    path0.reverse()
    path1.reverse()

    i = 0
    for i in range(min(len(path0), len(path1))):
        if path0[i] is not path1[i]: return path0[i-1]

    return path0[i]


@enable_executor_hook
def lca_wrapper(executor, tree, node0, node1):
    result = executor.run(
        functools.partial(lca, must_find_node(tree, node0),
                          must_find_node(tree, node1)))

    if result is None:
        raise TestFailure('Result can\'t be None')
    return result.data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('lowest_common_ancestor_with_parent.py',
                                       'lowest_common_ancestor.tsv',
                                       lca_wrapper))
