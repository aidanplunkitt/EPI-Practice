from test_framework import generic_test
from test_framework.test_failure import TestFailure

import functools
import string

def int_to_string(x: int) -> str:
    is_negative = False
    if x < 0:
        x, is_negative = -x, True

    s = []
    # doing while True instead of while x covers edge case of argument 0 given
    # essentially a do-while now, as x==0 checked at end of loop rather than start
    while True:
        s.append(chr(ord('0') + x % 10))
        x //= 10
        if x == 0:
            break

    return ('-' if is_negative else '') + ''.join(reversed(s))


def string_to_int(s: str) -> int:
    return functools.reduce(lambda running_sum, c: running_sum * 10 + string.digits.index(c), s[s[0] == '-' or s[0] == '+':], 0) * (-1 if s[0] == '-' else 1)


def wrapper(x, s):
    if int(int_to_string(x)) != x:
        raise TestFailure('Int to string conversion failed')
    if string_to_int(s) != x:
        raise TestFailure('String to int conversion failed')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('string_integer_interconversion.py',
                                       'string_integer_interconversion.tsv',
                                       wrapper))
