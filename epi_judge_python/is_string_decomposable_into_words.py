import functools
from typing import List, Set

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

# 16.7, O(n^3) time (n being length of domain), O(n) space
def decompose_into_dictionary_words(domain: str,
                                    dictionary: Set[str]) -> List[str]:
    word_lens = [-1] * len(domain)
    for i in range(len(domain)):
        if domain[:i+1] in dictionary:
            word_lens[i] = i + 1
            continue

        for j in range(i):
            if word_lens[j] != -1 and domain[j+1:i+1] in dictionary:
                word_lens[i] = i - j
                break

    words = []
    if word_lens[-1] != -1:
        i = len(domain) - 1
        while i >= 0:
            words.append(domain[i + 1 - word_lens[i]:i + 1])
            i -= word_lens[i]
    return words[::-1]


@enable_executor_hook
def decompose_into_dictionary_words_wrapper(executor, domain, dictionary,
                                            decomposable):
    result = executor.run(
        functools.partial(decompose_into_dictionary_words, domain, dictionary))

    if not decomposable:
        if result:
            raise TestFailure('domain is not decomposable')
        return

    if any(s not in dictionary for s in result):
        raise TestFailure('Result uses words not in dictionary')

    if ''.join(result) != domain:
        raise TestFailure('Result is not composed into domain')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_string_decomposable_into_words.py',
            'is_string_decomposable_into_words.tsv',
            decompose_into_dictionary_words_wrapper))
