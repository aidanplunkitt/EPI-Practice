from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def reverse_sublist(L: ListNode, start: int,
                    finish: int) -> Optional[ListNode]:
    if (finish - start) < 1: return L

    ph = ListNode()
    ph.next = L
    L = ph

    for _ in range(1, start):
        L = L.next

    prev, r_tail, t = L, L.next, L.next.next
    r_head, t_next = r_tail, t
    for _ in range(finish - start):
        t_next = t.next
        t.next = r_head
        r_head = t
        t = t_next
    prev.next, r_tail.next = r_head, t
    return ph.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_sublist.py',
                                       'reverse_sublist.tsv', reverse_sublist))
