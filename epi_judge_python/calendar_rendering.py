import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

# Event is a tuple (start_time, end_time)
Event = collections.namedtuple('Event', ('start', 'finish'))

# 13.6, O(n log n) time, O(n) space
def find_max_simultaneous_events(A: List[Event]) -> int:
    times = []
    for event in A:
        times.append((event.start, True))
        times.append((event.finish, False))

    times.sort(key=lambda time: (time[0], not time[1]))

    running_sum = max_sum = 0
    for time in times:
        if time[1]:
            running_sum += 1
            max_sum = max(max_sum, running_sum)
        else:
            running_sum -= 1

    return max_sum

@enable_executor_hook
def find_max_simultaneous_events_wrapper(executor, events):
    events = [Event(*x) for x in events]
    return executor.run(functools.partial(find_max_simultaneous_events,
                                          events))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('calendar_rendering.py',
                                       'calendar_rendering.tsv',
                                       find_max_simultaneous_events_wrapper))
