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
        if self.freq == other.freq:
            return self.string < other.string
        # inverting the sign, greater than instead of less than helps with making max_heap
        return self.freq > other.freq

def k_most_frequent_strings(strs: List[str], k: int) -> List[str]:
    # max heap
    max_heap = []
    freqs = Counter(strs)
    max_heap = [Pair(s, freq) for s, freq in freqs.items()]
    heapq.heapify(max_heap)

    return [heapq.heappop(max_heap).string for _ in range(k)]