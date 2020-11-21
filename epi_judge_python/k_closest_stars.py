import functools
import math
from typing import Iterator, List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

import itertools
import heapq

class Star:
    def __init__(self, x: float, y: float, z: float) -> None:
        self.x, self.y, self.z = x, y, z

    @property
    def distance(self) -> float:
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def __lt__(self, rhs: 'Star') -> bool:
        return self.distance < rhs.distance

    def __repr__(self):
        return str(self.distance)

    def __str__(self):
        return self.__repr__()

    def __eq__(self, rhs):
        return math.isclose(self.distance, rhs.distance)

# 10.4, O(n log k) time, O(k) space
def find_closest_k_stars(stars: Iterator[Star], k: int) -> List[Star]:
    # negate entries to turn python heapq minheap into maxheap, to quickly retrieve the largest of the k mins for comparison
    starheap = [(s.distance * -1.0, s) for s in itertools.islice(stars, k)]
    heapq.heapify(starheap)

    for s in stars:
        # only do log k heap push work when a new k-min is actually found
        if s.distance < (starheap[0][0] * -1.0):
            heapq.heappushpop(starheap, (s.distance * -1.0, s))

    ans = [s for _, s in starheap]
    return ans[::-1]

def comp(expected_output, output):
    if len(output) != len(expected_output):
        return False
    return all(
        math.isclose(s.distance, d)
        for s, d in zip(sorted(output), expected_output))


@enable_executor_hook
def find_closest_k_stars_wrapper(executor, stars, k):
    stars = [Star(*a) for a in stars]
    return executor.run(functools.partial(find_closest_k_stars, iter(stars),
                                          k))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('k_closest_stars.py',
                                       'k_closest_stars.tsv',
                                       find_closest_k_stars_wrapper, comp))
