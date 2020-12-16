from typing import List

from test_framework import generic_test

ADJACENT = [(1,0), (-1,0), (0,1), (0,-1)]

# 18.2, O(V + E) time, O(V) space ?
def flip_color(x: int, y: int, image: List[List[bool]]) -> None:
    def dfs(x,y):
        image[x][y] = not color
        for dx, dy in ADJACENT:
            if 0 <= x + dx < len(image) and 0 <= y + dy < len(image[0]) \
                and image[x+dx][y+dy] is color:
                dfs(x+dx, y+dy)

    color = image[x][y]
    dfs(x,y)



def flip_color_wrapper(x, y, image):
    flip_color(x, y, image)
    return image


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('matrix_connected_regions.py',
                                       'painting.tsv', flip_color_wrapper))
