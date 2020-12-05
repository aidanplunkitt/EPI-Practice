from test_framework import generic_test

import functools

# 16.0, O(n) time, O(n) space for cache
@functools.lru_cache(None)
def fibonacci(n: int) -> int:
    if n < 2:
        return n

    return fibonacci(n-1) + fibonacci(n-2)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('fibonacci.py', 'fibonacci.tsv',
                                       fibonacci))
