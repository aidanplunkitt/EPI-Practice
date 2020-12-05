from test_framework import generic_test

# 16.0, O(n) time, O(n) space for cache
def fibonacci(n: int) -> int:
    cache = [0,1] + [-1] * (n-1)
    def helper(i):
        if i < 2:
            return i
        if cache[i] != -1:
            return cache[i]

        cache[i] = helper(i-1) + helper(i-2)
        return cache[i]

    return helper(n)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('fibonacci.py', 'fibonacci.tsv',
                                       fibonacci))
