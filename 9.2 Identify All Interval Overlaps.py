from ds import Interval
from typing import List

"""
Definition of Interval:
class Interval:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end
"""

def identify_all_interval_overlaps(intervals1: List[Interval], intervals2: List[Interval]) -> List[Interval]:
    overlaps = []
    i = j = 0
    while i < len(intervals1) and j < len(intervals2):
        if intervals1[i].start <= intervals2[j].start:
            A, B = intervals1[i], intervals2[j]
        else:
            B, A = intervals1[i], intervals2[j]
        
        # check overlap and merge accordingly
        # A.start < B.start
        if B.start <= A.end:
            overlaps.append(Interval(B.start, min(A.end, B.end)))
        if intervals1[i].end < intervals2[j].end:
            i += 1
        else:
            j += 1
    
    return overlaps