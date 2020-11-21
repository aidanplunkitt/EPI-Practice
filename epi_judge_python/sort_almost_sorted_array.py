from typing import Iterator, List

from test_framework import generic_test

import itertools
import heapq

# 10.3, O(nlog2k) time, O(k) space (O(n) space for list to return)
def sort_approximately_sorted_array(sequence: Iterator[int],
                                    k: int) -> List[int]:
    heap = list(itertools.islice(sequence, 2*k))
    heapq.heapify(heap)

    ans = []
    for num in sequence:
        ans.append(heapq.heappushpop(heap, num))

    while heap:
        ans.append(heapq.heappop(heap))

    return ans


def sort_approximately_sorted_array_wrapper(sequence, k):
    return sort_approximately_sorted_array(iter(sequence), k)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'sort_almost_sorted_array.py', 'sort_almost_sorted_array.tsv',
            sort_approximately_sorted_array_wrapper))
