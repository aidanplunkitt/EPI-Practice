from test_framework import generic_test


def is_palindromic(s: str) -> bool:
    return all(a == b for a, b in zip(
        map(str.lower, filter(str.isalnum, s)),
        map(str.lower, filter(str.isalnum, reversed(s)))
    ))



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_string_palindromic.py',
                                       'is_string_palindromic.tsv',
                                       is_palindromic))
