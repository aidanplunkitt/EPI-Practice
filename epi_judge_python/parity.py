from test_framework import generic_test

def parity_no_lut(x: int) -> int:
    parity = 0
    while x:
        parity ^= 1
        # hack to reduce time complexity from O(n) where n is the num of bits, 
        # to O(k) where k is the num of 1s in binary string
        x &= x - 1

    return parity

# build 64K-entry LUT for better performance on sequences of large numbers
LUT_16BIT = [parity_no_lut(x) for x in range(pow(2,16))]
   
MASK_SIZE = 16
BIT_MASK = 0xFFFF

# O(n/L), where n is the size of the parameter and L is the size of the LUT entry, e.g. 64/16 == 4
def parity(x: int) -> int:
    # assuming 64-bit argument
    return  LUT_16BIT[x >> (3 * MASK_SIZE)] ^ \
            LUT_16BIT[(x >> (2 * MASK_SIZE)) & BIT_MASK] ^ \
            LUT_16BIT[(x >> MASK_SIZE) & BIT_MASK] ^ \
            LUT_16BIT[x & BIT_MASK]


if __name__ == '__main__':
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))
