from test_framework import generic_test


def is_well_formed(s: str) -> bool:
    parens = {
        '}': '{',
        ']': '[',
        ')': '('
    }

    stack = []
    for c in s:
        if c in parens:
            if not stack or parens[c] != stack.pop():
                return False
        else:
            stack.append(c)

    return False if stack else True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_valid_parenthesization.py',
                                       'is_valid_parenthesization.tsv',
                                       is_well_formed))
