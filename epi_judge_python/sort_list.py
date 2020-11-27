from typing import Optional

from list_node import ListNode
from test_framework import generic_test

# 13.11, O(n log n) time, O(log n) space (implicit callstack space)
def stable_sort_list(L: ListNode) -> Optional[ListNode]:
    if L is None or L.next is None:
        return L

    mid, tail = L, L.next
    while tail is not None and tail.next is not None:
        mid = mid.next
        tail = tail.next.next

    R, mid.next = mid.next, None
    L, R = stable_sort_list(L), stable_sort_list(R)
    dh = node = ListNode()
    while L and R:
        if L.data < R.data:
            node.next, L = L, L.next
        else:
            node.next, R = R, R.next
        node = node.next

    node.next = L or R
    return dh.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sort_list.py', 'sort_list.tsv',
                                       stable_sort_list))
