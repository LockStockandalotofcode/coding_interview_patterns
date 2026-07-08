from typing import List

def maximum_subarray_sum(nums: List[int]) -> int:
    n = len(nums)
    # DP method
    # base case
    if not nums:
        return 0
    
    # constructing dp array - for max_subarray_sums for all subarrays that end at index i
    dp = [0] * n
    # dp base case
    dp[0] = nums[0]
    max_sum = dp[0] 
    # why not float('-inf')
    # for single number input, since below loop never goes to 0-index element making it -inf
    # we are returned max_sum = -inf, which is inocrrect, and even in other cases, the comparison never truly occurs with nums[0], this subarray starting at 0 index is not included

    for idx in range(1, n):
        num = nums[idx]
        dp[idx] = max(dp[idx - 1] + num, num)
        max_sum = max(max_sum, dp[idx])
    
    return max_sum