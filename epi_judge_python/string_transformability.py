from typing import Set

from test_framework import generic_test

import collections
import string

# 18.7, O(s * D) time, O(D^2) space ?
def transform_string(D: Set[str], s: str, t: str) -> int:
    q = collections.deque([(s, 0)])
    D.remove(s)
    while q:
        orig, num = q.popleft()
        word = list(orig)
        for i, c in enumerate(word):
            for l in string.ascii_lowercase:
                word[i] = l
                key = ''.join(word)
                if key in D:
                    if key == t:
                        return num + 1
                    q.append((key, num + 1))
                    D.remove(key)
            word[i] = c
    
    return -1

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('string_transformability.py',
                                       'string_transformability.tsv',
                                       transform_string))
