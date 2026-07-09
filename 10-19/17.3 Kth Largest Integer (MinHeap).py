from typing import List
import heapq

def kth_largest_integer(nums: List[int], k: int) -> int:
    min_heap = []
    heapq.heapify(min_heap)

    for num in nums:
        if len(min_heap) < k:
            heapq.heappush(min_heap, num)
        elif num > min_heap[0]:
            heapq.heappop(min_heap)
            heapq.heappush(min_heap, num)
    
    return min_heap[0]