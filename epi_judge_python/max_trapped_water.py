from typing import List

from test_framework import generic_test

# 17.7, O(n) time, O(1) space
def get_max_trapped_water(heights: List[int]) -> int:
    i, j = 0, len(heights) - 1
    max_area = 0
    while i < j:
        max_area = max(max_area, (j - i) * min(heights[i], heights[j]))
        if heights[i] <= heights[j]:
            i += 1
        else:
            j -= 1
    return max_area


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('max_trapped_water.py',
                                       'max_trapped_water.tsv',
                                       get_max_trapped_water))
