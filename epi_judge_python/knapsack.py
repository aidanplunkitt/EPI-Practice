import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

Item = collections.namedtuple('Item', ('weight', 'value'))


def optimum_subject_to_capacity(items: List[Item], capacity: int) -> int:
    items.sort(key=lambda item: item[1] / item[0], reverse=True)

    def helper(weight, index):
        if weight == 0: return 0

        while items[index][0] > weight:
            index += 1
            if index == len(items): return 0

        return items[index][1] + helper(weight - items[index][0], index + 1)

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
