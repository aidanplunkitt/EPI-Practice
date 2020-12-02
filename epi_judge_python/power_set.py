from typing import List

from test_framework import generic_test, test_utils

# 15.4, O(2^n) time and space
def generate_power_set(input_set: List[int]) -> List[List[int]]:
    def helper(i):
        if i < len(input_set):
            tmp = []
            for item in s:
                tmp.append(item + [input_set[i]])
            s.extend(tmp)
            helper(i + 1)

    s = [[]]
    helper(0)
    return s


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('power_set.py', 'power_set.tsv',
                                       generate_power_set,
                                       test_utils.unordered_compare))
