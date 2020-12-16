from typing import List

from test_framework import generic_test

ADJ = [(1,0),(-1,0),(0,1),(0,-1)]

# 18.3, O(nm) time and space
def fill_surrounded_regions(board: List[List[str]]) -> None:
    def dfs(x,y):
        if board[x][y] == 'W':
            board[x][y] = ''
            for dx, dy in ADJ:
                if 0 <= x+dx < n and 0 <= y+dy < m:
                    dfs(x+dx,y+dy)

    n, m = len(board), len(board[0])
    for i in range(n):
            dfs(i,0)
            dfs(i, m-1)
    for j in range(m):
            dfs(0,j)
            dfs(n-1,j)

    board[:] = [['B' if c else 'W' for c in row] for row in board]



def fill_surrounded_regions_wrapper(board):
    fill_surrounded_regions(board)
    return board


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('matrix_enclosed_regions.py',
                                       'matrix_enclosed_regions.tsv',
                                       fill_surrounded_regions_wrapper))
