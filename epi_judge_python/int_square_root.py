from test_framework import generic_test

# 11.4, O(log k) time, O(1) space
def square_root(k: int) -> int:
    left, right = 0, k

    while left <= right:
        mid = (left + right) // 2
        num = mid * mid
        if num == k:
            return mid
        elif num < k:
            left = mid + 1
        else: # num > k
            right = mid - 1

    return left - 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_square_root.py',
                                       'int_square_root.tsv', square_root))
