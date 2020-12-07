import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

Item = collections.namedtuple('Item', ('weight', 'value'))

# 16.6, O(mn) time and space
def optimum_subject_to_capacity(items: List[Item], capacity: int) -> int:
    cache = [[0] * len(items) for _ in range(capacity + 1)]
    def helper(cap, index):
        if index == len(items):
            return 0
        if val := cache[cap][index]:
            return val
        without_item = helper(cap, index + 1)
        with_item = 0 if cap < items[index].weight else helper(cap - items[index].weight, index + 1) + items[index].value
        cache[cap][index] = max(without_item, with_item)
        return cache[cap][index]

    return helper(capacity, 0)


@enable_executor_hook
def optimum_subject_to_capacity_wrapper(executor, items, capacity):
    items = [Item(*i) for i in items]
    return executor.run(
        functools.partial(optimum_subject_to_capacity, items, capacity))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('knapsack.py', 'knapsack.tsv',
                                       optimum_subject_to_capacity_wrapper))
