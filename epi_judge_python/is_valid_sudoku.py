from typing import List

from test_framework import generic_test


# Check if a partially filled matrix has any conflicts.
def is_valid_sudoku(partial_assignment: List[List[int]]) -> bool:
    def validate_rows(m):
        for row in m:
            ht = [0] * 10
            for e in row:
                if e != 0 and ht[e]:
                    return False
                else:
                    ht[e] = 1
        return True

    # TODO
    def validate_square(m):
        return True

    # check rows
    if not validate_rows(partial_assignment): return False

    # transpose matrix to apply validate_rows to columns
    transposed = list(zip(*partial_assignment))
    if not validate_rows(transposed): return False


    ## TODO
    # for x in range(3):
    #     for y in range(3):
    #         m = partial_assignment[x*3:x*3+3, y*3:y*3+3]
    #         if not validate_square(m): return False

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_valid_sudoku.py',
                                       'is_valid_sudoku.tsv', is_valid_sudoku))
