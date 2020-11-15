from typing import List

from test_framework import generic_test, test_utils

import string

phone_map = [['0'], ['1'], ['A','B','C'], ['D','E','F'], ['G','H','I'], ['J','K','L'], ['M','N','O'], ['P','Q','R','S'], ['T','U','V'], ['W','X','Y','Z']]

def phone_mnemonic(phone_number: str) -> List[str]:
    num = string.digits.index(phone_number[-1])

    if len(phone_number) == 1:
        return phone_map[num]

    return [A + b for A in phone_mnemonic(phone_number[:-1]) for b in phone_map[num]]    


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'phone_number_mnemonic.py',
            'phone_number_mnemonic.tsv',
            phone_mnemonic,
            comparator=test_utils.unordered_compare))
