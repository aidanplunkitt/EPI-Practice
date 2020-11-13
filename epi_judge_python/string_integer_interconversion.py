from test_framework import generic_test
from test_framework.test_failure import TestFailure


def int_to_string(x: int) -> str:
    s = ''
    signed = False

    if x == 0: return '0'

    if x < 0:
        signed = True
        x *= -1

    while x:
        x, c = divmod(x, 10)
        s += (chr(ord('0') + c))

    if signed: s += '-'

    return s[::-1]

    


def string_to_int(s: str) -> int:
    i = 0
    val = 0
    signedness = 1
    if s[i] == '-':
        signedness = -1
        i = 1
    
    if s[i] == '+':
        i = 1

    while i < len(s):
        val = val * 10 + (ord(s[i]) - ord('0'))
        i += 1

    return val * signedness

    


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
