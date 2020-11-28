from typing import List

from test_framework import generic_test

# 15.2
def n_queens(n: int) -> List[List[int]]:
    def solve_n_queens(row):
        if row == n:
            valid_placements.append(board.copy())
            return
        for col in range(n):
            if all(
                    # if not in a vertical or diagonal line with a queen from an above row
                    abs(c - col) not in (0, row - i) 
                    # for every previous row
                    for i, c in enumerate(board[:row])):
                # mark this as a valid placement for this row
                board[row] = col
                # solve for next row
                solve_n_queens(row + 1)

    valid_placements = []
    board = [0] * n
    solve_n_queens(0)
    return valid_placements


def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('n_queens.py', 'n_queens.tsv', n_queens,
                                       comp))
