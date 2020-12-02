import copy
import functools
import math
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

# 15.9, exponential runtime ?, O(n) callstack space where n is num of empty entries in sudoku puzzle
def solve_sudoku(partial_assignment: List[List[int]]) -> bool:
    def is_valid(val, i, j):
        # check row
        for entry in partial_assignment[i]:
            if entry == val: return False

        # check column
        for row in partial_assignment:
            if row[j] == val: return False

        # check matrix
        x, y = i // 3 * 3, j // 3 * 3
        for a in range(3):
            for b in range(3):
                if partial_assignment[x + a][y + b] == val:
                    return False
                
        return True

    def solve_partial(i, j):
        if j == 9:
            i, j = i + 1, 0
            if i == 9:
                return True

        if partial_assignment[i][j] != 0:
            return solve_partial(i, j + 1)

        # handle empty square
        for val in range(1,10):
            if is_valid(val, i, j):
                partial_assignment[i][j] = val
                if solve_partial(i, j + 1):
                    return True
        partial_assignment[i][j] = 0
        return False


    return solve_partial(0,0)

def assert_unique_seq(seq):
    seen = set()
    for x in seq:
        if x == 0:
            raise TestFailure('Cell left uninitialized')
        if x < 0 or x > len(seq):
            raise TestFailure('Cell value out of range')
        if x in seen:
            raise TestFailure('Duplicate value in section')
        seen.add(x)


def gather_square_block(data, block_size, n):
    block_x = (n % block_size) * block_size
    block_y = (n // block_size) * block_size

    return [
        data[block_x + i][block_y + j] for j in range(block_size)
        for i in range(block_size)
    ]


@enable_executor_hook
def solve_sudoku_wrapper(executor, partial_assignment):
    solved = copy.deepcopy(partial_assignment)

    executor.run(functools.partial(solve_sudoku, solved))

    if len(partial_assignment) != len(solved):
        raise TestFailure('Initial cell assignment has been changed')

    for (br, sr) in zip(partial_assignment, solved):
        if len(br) != len(sr):
            raise TestFailure('Initial cell assignment has been changed')
        for (bcell, scell) in zip(br, sr):
            if bcell != 0 and bcell != scell:
                raise TestFailure('Initial cell assignment has been changed')

    block_size = int(math.sqrt(len(solved)))
    for i, solved_row in enumerate(solved):
        assert_unique_seq(solved_row)
        assert_unique_seq([row[i] for row in solved])
        assert_unique_seq(gather_square_block(solved, block_size, i))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sudoku_solve.py', 'sudoku_solve.tsv',
                                       solve_sudoku_wrapper))
