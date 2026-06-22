from typing import List

def pair_sum_unsorted(nums: List[int], target: int) -> List[int]:
    # HASH MAP : number -> index
    nums_map = {}

    for idx, num in enumerate(nums):
        complement = target - num 
        if complement in nums_map:
            return [ nums_map[complement], idx]
            
        
        nums_map[num] = idx
    
    return []