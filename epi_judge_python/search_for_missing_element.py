import collections
from typing import List

from test_framework import generic_test
from test_framework.test_failure import PropertyName

DuplicateAndMissing = collections.namedtuple('DuplicateAndMissing',
                                             ('duplicate', 'missing'))

# 11.10, O(n) time, O(1) space
def find_duplicate_missing(A: List[int]) -> DuplicateAndMissing:
    enumerate_xor = array_xor = 0
    for i, a in enumerate(A):
        enumerate_xor ^= i
        array_xor ^= a

    # XOR all values of the array with all values in [0,n) where n = len(array)
    combined_xor = enumerate_xor ^ array_xor
    diff_lsb = combined_xor & ~(combined_xor - 1)

    # find all values that contain a bit within the combined_xor above (in this case the LSB), and xor together
    enum_bit_xor = array_bit_xor = 0
    for i, a in enumerate(A):
        if i & diff_lsb:
            enum_bit_xor ^= i
        if a & diff_lsb:
            array_bit_xor ^= a

    # voodoo
    duplicate = enum_bit_xor ^ array_bit_xor # this value is either the duplicate or the missing
    missing = combined_xor ^ duplicate # and the other value can be recovered from the original combined_xor

    # swap if our 50/50 guess was wrong
    if duplicate not in A:
        duplicate, missing = missing, duplicate

    return DuplicateAndMissing(duplicate, missing)


def res_printer(prop, value):
    def fmt(x):
        return 'duplicate: {}, missing: {}'.format(x[0], x[1]) if x else None

    return fmt(value) if prop in (PropertyName.EXPECTED,
                                  PropertyName.RESULT) else value


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_for_missing_element.py',
                                       'find_missing_and_duplicate.tsv',
                                       find_duplicate_missing,
                                       res_printer=res_printer))
