from typing import List

def k_sum_subarrays(nums: List[int], k: int) -> int:
    n = len(nums)
    count = 0

    # populate prefix array
    prefix_sum = [0]
    for i in range(1, n+1):
        prefix_sum.append(prefix_sum[i-1] + nums[i-1])

    # loop through all subarrays
    for i in range(1, n+1):
        for j in range(1, i+1):
            if prefix_sum[i] - prefix_sum[j-1] == k:
                count += 1
            
    return count