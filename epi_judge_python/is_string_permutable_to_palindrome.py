from test_framework import generic_test

import collections

# 12.1, O(n) time, O(n) space
def can_form_palindrome(s: str) -> bool:
    letters = collections.Counter(c for c in s if c.isalpha())

    odd = 0
    for _, count in letters.items():
        if count % 2 == 1:
            odd += 1

    return odd < 2


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_string_permutable_to_palindrome.py',
            'is_string_permutable_to_palindrome.tsv', can_form_palindrome))
