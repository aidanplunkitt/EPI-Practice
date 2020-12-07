from typing import List

from test_framework import generic_test

import functools

# 16.5, O(n^2 * m) time? and space?
def is_pattern_contained_in_grid(grid: List[List[int]],
                                 pattern: List[int]) -> bool:
    @functools.lru_cache(None)
    def helper(x, y, pattern_idx):
        if pattern_idx == len(pattern):
            return True

        return any([
            x - 1 >= 0              and grid[x-1][y] == pattern[pattern_idx] and helper(x-1, y, pattern_idx + 1), # up
            x + 1 < len(grid)       and grid[x+1][y] == pattern[pattern_idx] and helper(x+1, y, pattern_idx + 1), # down
            y - 1 >= 0              and grid[x][y-1] == pattern[pattern_idx] and helper(x, y-1, pattern_idx + 1), # left
            y + 1 < len(grid[0])    and grid[x][y+1] == pattern[pattern_idx] and helper(x, y+1, pattern_idx + 1), # right
        ])

    for i, row in enumerate(grid):
        for j, col in enumerate(row):
            if col == pattern[0]:
                if valid := helper(i, j, 1):
                    return valid
    return False

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_string_in_matrix.py',
                                       'is_string_in_matrix.tsv',
                                       is_pattern_contained_in_grid))
