from test_framework import generic_test

import collections

# 12.1, O(n) time, O(n) space
def can_form_palindrome(s: str) -> bool:
    return sum(n % 2 for n in collections.Counter(s).values()) < 2


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_string_permutable_to_palindrome.py',
            'is_string_permutable_to_palindrome.tsv', can_form_palindrome))
