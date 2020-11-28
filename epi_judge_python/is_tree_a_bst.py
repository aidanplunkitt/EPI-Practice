from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

import collections

# 14.1, O(n) time, O(n) space
def is_binary_tree_bst(tree: BinaryTreeNode) -> bool:
    if not tree: return True
    
    q = collections.deque()
    q.append((tree,(float('-inf'), float('inf'))))

    # BFS
    while q:
        node = q.popleft()            
        if not node[1][0] <= node[0].data <= node[1][1]:
            return False
        if node[0].left:
            q.append((node[0].left, (node[1][0], node[0].data)))
        if node[0].right:
            q.append((node[0].right, (node[0].data, node[1][1])))

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_a_bst.py', 'is_tree_a_bst.tsv',
                                       is_binary_tree_bst))
