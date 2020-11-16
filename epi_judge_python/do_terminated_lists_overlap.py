import functools

from list_node import ListNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def overlapping_no_cycle_lists(l0: ListNode, l1: ListNode) -> ListNode:
    if not (l0 and l1): return None
    tail0, tail1 = l0, l1
    len0 = len1 = 1
    while tail0.next:
        tail0 = tail0.next
        len0 += 1
    while tail1.next:
        tail1 = tail1.next
        len1 += 1

    if tail0 is not tail1: return None

    for _ in range(abs(len0 - len1)):
        if len0 > len1:
            l0 = l0.next
        else:
            l1 = l1.next

    while l0 is not l1:
        l0 = l0.next
        l1 = l1.next

    return l0


@enable_executor_hook
def overlapping_no_cycle_lists_wrapper(executor, l0, l1, common):
    if common:
        if l0:
            i = l0
            while i.next:
                i = i.next
            i.next = common
        else:
            l0 = common

        if l1:
            i = l1
            while i.next:
                i = i.next
            i.next = common
        else:
            l1 = common

    result = executor.run(functools.partial(overlapping_no_cycle_lists, l0,
                                            l1))

    if result != common:
        raise TestFailure('Invalid result')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('do_terminated_lists_overlap.py',
                                       'do_terminated_lists_overlap.tsv',
                                       overlapping_no_cycle_lists_wrapper))
