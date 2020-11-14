from test_framework import generic_test


def is_palindromic(s: str) -> bool:
    i, j = 0, len(s) - 1

    while i < j:
        while not s[i].isalpha() and i < j:
            i += 1

        while not s[j].isalpha() and i < j:
            j -= 1

        if s[i].lower() != s[j].lower():
            return False

        i += 1
        j -= 1

    return True



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_string_palindromic.py',
                                       'is_string_palindromic.tsv',
                                       is_palindromic))
