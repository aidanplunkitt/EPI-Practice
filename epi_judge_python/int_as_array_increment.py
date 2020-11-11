from typing import List

from test_framework import generic_test


def plus_one(A: List[int]) -> List[int]:
    A.reverse()

    i=0
    while i < len(A) and A[i] == 9:
        A[i] = 0
        i += 1
    
    if i == len(A): # every number was a 9
        A.append(1)
    else:
        A[i] += 1

    return A[::-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_array_increment.py',
                                       'int_as_array_increment.tsv', plus_one))
