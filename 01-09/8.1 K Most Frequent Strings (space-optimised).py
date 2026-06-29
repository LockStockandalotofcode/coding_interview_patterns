from typing import List
import heapq
from collections import Counter
 # custom comparator for lexicographical order if same frequency
class Pair:
    def __init__(self, string: str, freq: int):
        self.string = string
        self.freq = freq 
    
    def __lt__(self, other): # CUSTOM COMPARATOR 
        # OVERRIDE GENERAL LESS THAN MAGIC METHOD
        # both signs are inverted when min_heap is used
        if self.freq == other.freq:
            return self.string > other.string
        # space optimised approach, with min heap
        return self.freq < other.freq

def k_most_frequent_strings(strs: List[str], k: int) -> List[str]:
    # min heap
    min_heap = []
    freqs = Counter(strs)
    for s, freq in freqs.items():
        heapq.heappush(min_heap, Pair(s, freq))
        if len(min_heap) > k:
            heapq.heappop(min_heap)

    res = [heapq.heappop(min_heap).string for _ in range(k)]
    res.reverse()
    return res