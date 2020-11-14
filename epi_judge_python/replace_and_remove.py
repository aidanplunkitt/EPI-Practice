import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


def replace_and_remove(size: int, s: List[str]) -> int:
    num_a = 0
    last_nonb = 0
    for i in range(size):
        if s[i] != 'b':
            if s[i] == 'a':
                num_a += 1
            s[i], s[last_nonb] = s[last_nonb], s[i]
            last_nonb += 1

    # [a,c,d,c,a,a,d,_,_,_,_]
    #                ^ last_nonb

    i = last_nonb + num_a - 1
    j = last_nonb - 1
    while j >= 0:
        s[i] = s[j]
        i -= 1
        if s[j] == 'a':
            s[i+1] = 'd'
            s[i] = 'd'
            i -= 1
        j -= 1

    return last_nonb + num_a


@enable_executor_hook
def replace_and_remove_wrapper(executor, size, s):
    res_size = executor.run(functools.partial(replace_and_remove, size, s))
    return s[:res_size]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('replace_and_remove.py',
                                       'replace_and_remove.tsv',
                                       replace_and_remove_wrapper))
