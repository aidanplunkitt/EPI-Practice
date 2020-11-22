from typing import Iterator, List

from test_framework import generic_test

import heapq

# 10.5, O(n log n) time, O(n) space
def online_median(sequence: Iterator[int]) -> List[float]:
    # lower_half is a maxheap
    ans, lower_half, higher_half = [], [], []

    for s in sequence:
        heapq.heappush(lower_half, heapq.heappushpop(higher_half, s) * -1)

        if len(lower_half) > len(higher_half):
            heapq.heappush(higher_half, heapq.heappop(lower_half) * -1)

        ans.append(higher_half[0] if len(higher_half) > len(lower_half) else (0.5 * (lower_half[0] * -1 + higher_half[0])))

    return ans


def online_median_wrapper(sequence):
    return online_median(iter(sequence))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('online_median.py', 'online_median.tsv',
                                       online_median_wrapper))
