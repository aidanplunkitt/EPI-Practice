from typing import List

from test_framework import generic_test

import heapq

def merge_sorted_arrays(sorted_arrays: List[List[int]]) -> List[int]:
    # minheap, iters = [], []
    # for i, arr in enumerate(sorted_arrays):
    #     iters.append(iter(arr))
    #     heapq.heappush(minheap, (next(iters[i], None), i))

    # sort = []
    # while minheap:
    #     smallest, smallest_i = heapq.heappop(minheap)
    #     sort.append(smallest)
    #     topush = next(iters[smallest_i], None)
    #     if topush is not None:
    #         heapq.heappush(minheap, (topush, smallest_i))

    # return sort
    return list(heapq.merge(*sorted_arrays))



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_arrays_merge.py',
                                       'sorted_arrays_merge.tsv',
                                       merge_sorted_arrays))
