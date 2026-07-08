from typing import List

def jump_to_the_end(nums: List[int]) -> bool:
    if not nums:
        return False
        
    destination_idx = len(nums) - 1 # initialising at the last num in array

    if len(nums) == 1:
        return True

    for i in range(len(nums) - 1, -1, -1):
        jump = nums[i]
        if i + jump >= destination_idx:
            destination_idx = i
    
    return destination_idx == 0 # only if we can reach start from end, then it means true
