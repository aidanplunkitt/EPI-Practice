from test_framework import generic_test

# 16.0, O(n) time, O(1) space
def fibonacci(n: int) -> int:
    fib2, fib1 = 0, 1
    for _ in range(n):
        fib1, fib2 = fib1 + fib2, fib1
    return fib2

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('fibonacci.py', 'fibonacci.tsv',
                                       fibonacci))
