from typing import List

from test_framework import generic_test

import heapq

def merge_sorted_arrays(sorted_arrays: List[List[int]]) -> List[int]:
    MAX_NUM_HEAP_ELEMENTS = 100
    combined, final = [0] * MAX_NUM_HEAP_ELEMENTS, []

    i, items_per_file = 0, MAX_NUM_HEAP_ELEMENTS // len(sorted_arrays)
    for a in sorted_arrays:
        # find a way to use prevmax to skip past already included items in individual subarrays, and find a smarter way
        # to fill up heap from the subarrays than with a precalculated constant num of elems from each subarray
        if (items_per_file * i) < len(a):
            for item in a[(items_per_file * i):min(items_per_file * (i+1), len(a))]:
                # make negative to use minheap as maxheap
                if (item * -1) < combined[0]:
                    heapq.heappushpop(combined, item * -1)

        i += 1
        combined = [n * -1 for n in combined if n < 0]
        final.extend(combined)
        # prevmax = combined[0]
    return final


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_arrays_merge.py',
                                       'sorted_arrays_merge.tsv',
                                       merge_sorted_arrays))
