from typing import List

def largest_container(heights: List[int]) -> int:
    if not heights:
        return 0

    max_vol = 0
    curr_vol = 0
    left, right = 0, len(heights) - 1 # 0-based indexing

    while left < right:
        if heights[left] == 0:
            left += 1
            continue
        if heights[right] == 0:
            right -= 1
            continue
        
        curr_vol = min(heights[left], heights[right]) * (right - left)
        max_vol = max(max_vol, curr_vol)
        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1

    return max_vol