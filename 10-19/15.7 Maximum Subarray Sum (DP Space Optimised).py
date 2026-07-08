from typing import List

def maximum_subarray_sum(nums: List[int]) -> int:
    # Space Optimised DP method
    # base case
    if not nums:
        return 0
    
    # initialising with starting value as per traversal method
    current_subarray_sum = max_sum = nums[0] 

    # only keeping the immediate last subarray's max sum for optimisation
    for num in nums[1 : ]:
        current_subarray_sum = max(current_subarray_sum + num, num)
        max_sum = max(max_sum, current_subarray_sum)
    
    return max_sum