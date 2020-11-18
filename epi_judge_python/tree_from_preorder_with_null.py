import functools
from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

def reconstruct_preorder(preorder: List[int]) -> BinaryTreeNode:
    class Helper:
        """ Class to allow for static variable i to be used through recursive calls
            Apparently classes are the correct/only way to have static variables
        """
        def __init__(self, i):
            self.i = i

        def __call__(self):
            node = None
            if self.i < len(preorder):
                self.i += 1
                if preorder[self.i-1]:
                    node = BinaryTreeNode(preorder[self.i-1])
                    node.left = self.__call__()
                    node.right = self.__call__()

            return node
    
    ans = Helper(0)
    return ans()


@enable_executor_hook
def reconstruct_preorder_wrapper(executor, data):
    data = [None if x == 'null' else int(x) for x in data]
    return executor.run(functools.partial(reconstruct_preorder, data))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_from_preorder_with_null.py',
                                       'tree_from_preorder_with_null.tsv',
                                       reconstruct_preorder_wrapper))
