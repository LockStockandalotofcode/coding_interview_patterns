from typing import List

def maximum_subarray_sum(nums: List[int]) -> int:
    # KADANE's
    # base case
    if not nums:
        return 0
    
    curr_sum = max_sum = float('-inf')
    for num in nums:
        curr_sum = max(curr_sum + num, num)
        max_sum = max(max_sum, curr_sum)
    
    return max_sum