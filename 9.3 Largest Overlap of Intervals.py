from ds import Interval
from typing import List

"""
Definition of Interval:
class Interval:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end
"""

def largest_overlap_of_intervals(intervals: List[Interval]) -> int:
    # create a marked sorted array of start, end points
    # traverse through this array, tracking active intervals and updating max_active at every iteration
    # end point given priority over start point, when both falling at same time point

    points = []
    for interval in intervals:
        points.append((interval.start, 'S'))
        points.append((interval.end, 'E'))

    points.sort(key=lambda x: (x[0], x[1]))
    active_intervals = 0
    max_active = 0

    for point, point_type in points:
        if point_type == 'S':
            active_intervals += 1
        else:
            active_intervals -= 1
            
        max_active = max(max_active, active_intervals)

    return max_active