from typing import List

from test_framework import generic_test

# 12.5, O(n) time, O(n) space
def find_nearest_repetition(paragraph: List[str]) -> int:
    d, mindist = {}, float('inf')

    for i, word in enumerate(paragraph):
        if word in d:
            mindist = min(mindist, i - d[word])
        d[word] = i

    return mindist if mindist != float('inf') else -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('nearest_repeated_entries.py',
                                       'nearest_repeated_entries.tsv',
                                       find_nearest_repetition))
