import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

MPG = 20

# 17.6, O(n) time, O(1) space
# gallons[i] is the amount of gas in city i, and distances[i] is the
# distance city i to the next city.
def find_ample_city(gallons: List[int], distances: List[int]) -> int:
    running_sum = min_sum = index_after_min = 0
    for i in range(len(distances)):
        running_sum += gallons[i] * MPG - distances[i]
        if running_sum < min_sum:
            min_sum, index_after_min = running_sum, i + 1

    return index_after_min % len(distances)



@enable_executor_hook
def find_ample_city_wrapper(executor, gallons, distances):
    result = executor.run(
        functools.partial(find_ample_city, gallons, distances))
    num_cities = len(gallons)
    tank = 0
    for i in range(num_cities):
        city = (result + i) % num_cities
        tank += gallons[city] * MPG - distances[city]
        if tank < 0:
            raise TestFailure('Out of gas on city {}'.format(i))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('refueling_schedule.py',
                                       'refueling_schedule.tsv',
                                       find_ample_city_wrapper))
