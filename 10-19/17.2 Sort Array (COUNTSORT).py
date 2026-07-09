from typing import List
from random import randint

def sort_array(nums: List[int]) -> List[int]:
    # COUNT SORT FOR bound cases, bounds on type of elements allowed
    if not nums:
        return []
    
    # count freq of each number 
    freqs = [0] * (max(nums) + 1)
    for num in nums:
        freqs[num] += 1

    # build sorted array
    res = []
    for idx, freq in enumerate(freqs):
        res.extend([idx] * freq)
    
    return res