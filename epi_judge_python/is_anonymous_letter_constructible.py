from test_framework import generic_test

import collections

# 12.2, O(n + m) time, O(m) space
def is_letter_constructible_from_magazine(letter_text: str,
                                          magazine_text: str) -> bool:
    magazine_chars = collections.Counter(magazine_text)

    for c in letter_text:
        if not magazine_chars[c]:
            return False
        magazine_chars[c] -= 1

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_anonymous_letter_constructible.py',
            'is_anonymous_letter_constructible.tsv',
            is_letter_constructible_from_magazine))
