import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

Endpoint = collections.namedtuple('Endpoint', ('is_closed', 'val'))

Interval = collections.namedtuple('Interval', ('left', 'right'))

# 13.8, O(n log n) time, O(n) space
def union_of_intervals(intervals: List[Interval]) -> List[Interval]:
    intervals.sort(key=lambda i: (i.left.val, not i.left.is_closed))
    result = [intervals[0]]
    for i in intervals:
        j = result[-1]
        if i.left.val < j.right.val or \
          (i.left.val == j.right.val and \
          (i.left.is_closed or j.right.is_closed)):
            if i.right.val > j.right.val or \
              (i.right.val == j.right.val and i.right.is_closed):
                result[-1] = Interval(j.left, i.right)
        else:
            result.append(i)
    return result


@enable_executor_hook
def union_of_intervals_wrapper(executor, intervals):
    intervals = [
        Interval(Endpoint(x[1], x[0]), Endpoint(x[3], x[2])) for x in intervals
    ]

    result = executor.run(functools.partial(union_of_intervals, intervals))

    return [(i.left.val, i.left.is_closed, i.right.val, i.right.is_closed)
            for i in result]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('intervals_union.py',
                                       'intervals_union.tsv',
                                       union_of_intervals_wrapper))
