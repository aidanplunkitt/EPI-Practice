import collections
import copy
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

WHITE, BLACK = range(2)
DIRECTIONS = [(0,1), (0,-1), (1,0), (-1,0)]

Coordinate = collections.namedtuple('Coordinate', ('x', 'y'))

# 18.1 O((nm)!) time?, O(nm) space for cache / callstack
def search_maze(maze: List[List[int]], s: Coordinate,
                e: Coordinate) -> List[Coordinate]:
    tried = [[False] * len(maze[0]) for _ in maze]
    def dfs(v, seen):
        if v == e:
            return [e]

        i, j = v
        if tried[i][j]: return []

        neighbors = [Coordinate(i + dx, j + dy) \
            for dx, dy in DIRECTIONS \
                if (0 <= i + dx < len(maze) and 0 <= j + dy < len(maze[0])) \
                    and maze[i+dx][j+dy] is WHITE \
                    and Coordinate(i+dx, j+dy) not in seen]

        for n in neighbors:
            if path := dfs(n, seen | {n}):
                return path + [v]
        
        tried[i][j] = True
        return []
  
    seen = set([s])
    path = dfs(s, seen)[::-1]
    return path




def path_element_is_feasible(maze, prev, cur):
    if not ((0 <= cur.x < len(maze)) and
            (0 <= cur.y < len(maze[cur.x])) and maze[cur.x][cur.y] == WHITE):
        return False
    return cur == (prev.x + 1, prev.y) or \
           cur == (prev.x - 1, prev.y) or \
           cur == (prev.x, prev.y + 1) or \
           cur == (prev.x, prev.y - 1)


@enable_executor_hook
def search_maze_wrapper(executor, maze, s, e):
    s = Coordinate(*s)
    e = Coordinate(*e)
    cp = copy.deepcopy(maze)

    path = executor.run(functools.partial(search_maze, cp, s, e))

    if not path:
        return s == e

    if path[0] != s or path[-1] != e:
        raise TestFailure('Path doesn\'t lay between start and end points')

    for i in range(1, len(path)):
        if not path_element_is_feasible(maze, path[i - 1], path[i]):
            raise TestFailure('Path contains invalid segments')

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_maze.py', 'search_maze.tsv',
                                       search_maze_wrapper))
