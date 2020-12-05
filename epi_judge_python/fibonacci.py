from test_framework import generic_test

# 16.0, O(n) time, O(n) space for cache
def fibonacci(n: int) -> int:
    def helper(i, cache=[0,1]):
        if i < len(cache):
            return cache[i]
        cache.append(helper(i-1) + helper(i-2))
        return cache[i]

    return helper(n)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('fibonacci.py', 'fibonacci.tsv',
                                       fibonacci))
