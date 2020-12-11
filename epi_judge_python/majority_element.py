from typing import Iterator

from test_framework import generic_test

import collections

# 17.5 Find majority element, O(n) time, O(1) space
def majority_search(stream: Iterator[str]) -> str:
    majority = next(stream)
    count = 1
    for i, s in enumerate(stream):
        # i + 2 + 1
        # +2 because starting on second element in stream
        # +1 because we want to round up on odd elements // 2
        if count < (i + 3) // 2:
            majority = s
        if s == majority:
            count += 1

    return majority


def majority_search_wrapper(stream):
    return majority_search(iter(stream))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('majority_element.py',
                                       'majority_element.tsv',
                                       majority_search_wrapper))
