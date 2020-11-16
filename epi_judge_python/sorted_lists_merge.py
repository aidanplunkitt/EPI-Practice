from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def merge_two_sorted_lists(L1: Optional[ListNode],
                           L2: Optional[ListNode]) -> Optional[ListNode]:
    l = ListNode()
    ph = l

    while L1 or L2:
        if not L1:
            l.next = L2
            L2 = L2.next
        elif not L2:
            l.next = L1
            L1 = L1.next
        else:
            if L1.data < L2.data:
                l.next = L1
                L1 = L1.next
            else:
                l.next = L2
                L2 = L2.next
        l = l.next

    return ph.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_lists_merge.py',
                                       'sorted_lists_merge.tsv',
                                       merge_two_sorted_lists))
