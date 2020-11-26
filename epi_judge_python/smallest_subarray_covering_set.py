import collections
import functools
from typing import List, Set

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

Subarray = collections.namedtuple('Subarray', ('start', 'end'))

# 12.6, O(n) time (single pass), O(k) space (relative to size of keywords set)
def find_smallest_subarray_covering_set(paragraph: List[str],
                                        keywords: Set[str]) -> Subarray:
    min_len = float('inf')
    ret_val = Subarray(0, 0)
    d = {k: float('inf') for k in keywords}
    for i, word in enumerate(paragraph):
        if word in d:
            d[word] = i
            last_indices = list(d.values())
            if sum(last_indices) < float('inf'):
                enclosure_len = i - min(last_indices)
                if enclosure_len < min_len:
                    min_len = enclosure_len
                    ret_val = Subarray(i - enclosure_len, i)

    return ret_val


@enable_executor_hook
def find_smallest_subarray_covering_set_wrapper(executor, paragraph, keywords):
    copy = keywords

    (start, end) = executor.run(
        functools.partial(find_smallest_subarray_covering_set, paragraph,
                          keywords))

    if (start < 0 or start >= len(paragraph) or end < 0
            or end >= len(paragraph) or start > end):
        raise TestFailure('Index out of range')

    for i in range(start, end + 1):
        copy.discard(paragraph[i])

    if copy:
        raise TestFailure('Not all keywords are in the range')

    return end - start + 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'smallest_subarray_covering_set.py',
            'smallest_subarray_covering_set.tsv',
            find_smallest_subarray_covering_set_wrapper))
