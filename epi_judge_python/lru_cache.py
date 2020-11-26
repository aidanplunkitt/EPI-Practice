from test_framework import generic_test
from test_framework.test_failure import TestFailure

import collections

# 12.3, O(n) space (determined by capacity), O(1) time
class LruCache:
    def __init__(self, capacity: int) -> None:
        self._capacity = capacity
        self._cache = collections.OrderedDict()

    def lookup(self, isbn: int) -> int:
        if isbn not in self._cache:
            return -1
        price = self._cache.pop(isbn)
        self._cache[isbn] = price
        return price

    def insert(self, isbn: int, price: int) -> None:
        if isbn in self._cache:
            price = self._cache.pop(isbn)
        elif len(self._cache) == self._capacity:
            self._cache.popitem(last=False)
        self._cache[isbn] = price

    def erase(self, isbn: int) -> bool:
        return self._cache.pop(isbn, None) is not None


def lru_cache_tester(commands):
    if len(commands) < 1 or commands[0][0] != 'LruCache':
        raise RuntimeError('Expected LruCache as first command')

    cache = LruCache(commands[0][1])

    for cmd in commands[1:]:
        if cmd[0] == 'lookup':
            result = cache.lookup(cmd[1])
            if result != cmd[2]:
                raise TestFailure('Lookup: expected ' + str(cmd[2]) +
                                  ', got ' + str(result))
        elif cmd[0] == 'insert':
            cache.insert(cmd[1], cmd[2])
        elif cmd[0] == 'erase':
            result = 1 if cache.erase(cmd[1]) else 0
            if result != cmd[2]:
                raise TestFailure('Erase: expected ' + str(cmd[2]) + ', got ' +
                                  str(result))
        else:
            raise RuntimeError('Unexpected command ' + cmd[0])


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('lru_cache.py', 'lru_cache.tsv',
                                       lru_cache_tester))
