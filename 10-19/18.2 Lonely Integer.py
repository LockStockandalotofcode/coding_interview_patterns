from typing import List

def lonely_integer(nums: List[int]) -> int:
    res = 0

    for num in nums:
        res ^= num
    
    return res