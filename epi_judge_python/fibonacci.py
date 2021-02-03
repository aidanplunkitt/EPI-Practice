from test_framework import generic_test


def fibonacci(n: int) -> int:
    if n < 2:
        return n

    curr, last = 1, 0
    for _ in range(n - 1):
        curr, last = curr + last, curr

    return curr


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('fibonacci.py', 'fibonacci.tsv',
                                       fibonacci))
