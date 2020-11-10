from test_framework import generic_test


def reverse(x: int) -> int:
    r, sign = 0, 1
    
    if x < 0: 
        sign = -1
        x *= -1

    while x:
        r = r * 10 + (x % 10)
        x //= 10

    return r * sign


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_digits.py',
                                       'reverse_digits.tsv', reverse))
