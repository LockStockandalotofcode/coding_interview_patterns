from typing import List

def cutting_wood(heights: List[int], k: int) -> int:
    left = 0
    right = max(heights)
    while left < right:
        mid = (left + right) // 2 + 1
        if gets_enough_wood(mid, k, heights):
            left = mid
        else: 
            right = mid - 1
        # upper bound binary search :
        # here target  is gets_enough_wood returning True
        # if mid is False: move right, exclude mid
        # if mid is True, move left ptr, include mid
    return right
        
def gets_enough_wood(H: int, k: int, heights: List[int]) -> bool:
    # H height the cutter is set to
    # k minimum target required
    total_wood = 0
    for height in heights:
        if height > H:
            total_wood += height - H
    
    return total_wood >= k