from typing import Iterator

from test_framework import generic_test
from test_framework.test_failure import TestFailure

import itertools

# 11.9, O(n) time, O(2^16 * size(int) space)
def find_missing_element(stream: Iterator[int]) -> int:
    # copy iterator into queues so multiple passes can be made
    stream, stream_copy = itertools.tee(stream)

    # identify a 16-bit prefix with fewer than 2^16 (max) number of appearances in stream
    prefix_counts = [0] * 2**16
    for num in stream:
        prefix_counts[num >> 16] += 1

    prefix = 0
    for num in prefix_counts:
        if num < (2 ** 16):
            prefix = num
            break


    # identify a number with specified prefix that does not appear in stream
    suffix_counts = [0] * 2**16
    for num in stream_copy:
        if (num >> 16) == prefix:
            suffix_counts[num & 0xFFFF] = 1

    for i, num in enumerate(suffix_counts):
        if num == 0:
            return prefix << 16 + i

    # shouldn't get here
    return 0


def find_missing_element_wrapper(stream):
    try:
        res = find_missing_element(iter(stream))
        if res in stream:
            raise TestFailure('{} appears in stream'.format(res))
    except ValueError:
        raise TestFailure('Unexpected no missing element exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('absent_value_array.py',
                                       'absent_value_array.tsv',
                                       find_missing_element_wrapper))
