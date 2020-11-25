from test_framework import generic_test

import math

# 11.5, O(log x / s) time, where s it the tolerance in math.isclose(), O(1) space
def square_root(x: float) -> float:
    left, right = 1.0, x

    if x < 1.0:
        right, left = left, right

    while left <= right:
        mid = 0.5 * (left + right)
        square = mid * mid
        if math.isclose(x, square):
            return mid
        elif square > x:
            right = mid
        else:
            left = mid

    # shouldn't get here
    return -1.0


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('real_square_root.py',
                                       'real_square_root.tsv', square_root))
