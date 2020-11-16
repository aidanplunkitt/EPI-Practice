from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def even_odd_merge(L: ListNode) -> Optional[ListNode]:
    if not (L and L.next): return L

    even, odd, L = L, L.next, L.next.next
    h_even, h_odd = even, odd
    
    while L:
        even.next = L
        even = even.next
        L = L.next
        if L:
            odd.next = L
            odd = odd.next
            L = L.next

    even.next, odd.next = h_odd, None
    return h_even


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('even_odd_list_merge.py',
                                       'even_odd_list_merge.tsv',
                                       even_odd_merge))
