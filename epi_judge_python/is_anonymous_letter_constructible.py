from test_framework import generic_test

import collections

# 12.2, O(n + m) time, O(n + m) space
def is_letter_constructible_from_magazine(letter_text: str,
                                          magazine_text: str) -> bool:
    # subtracting collection.Counters returns a dict containing any positive differences
    # thus if letter_text has any surplus chars after subtracting magazine_text, we know magazine doesn't have all required chars
    return not (collections.Counter(letter_text) - collections.Counter(magazine_text))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_anonymous_letter_constructible.py',
            'is_anonymous_letter_constructible.tsv',
            is_letter_constructible_from_magazine))
