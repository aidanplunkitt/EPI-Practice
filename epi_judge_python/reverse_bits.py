from test_framework import generic_test

def reverse_16(x: int) -> int:
    result = 0
    for _ in range(16):
        result = (result << 1) + (x & 1)
        x >>= 1

    return result

LUT_16 = [reverse_16(x) for x in range(2 ** 16)]
MASK = 0xFFFF
WORD_SIZE = 16

def reverse_bits(x: int) -> int:
    # assume 64-bit arg
    result = 0
    for _ in range(4):
        result = (result << WORD_SIZE) + LUT_16[x & MASK]
        x >>= WORD_SIZE

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_bits.py', 'reverse_bits.tsv',
                                       reverse_bits))
