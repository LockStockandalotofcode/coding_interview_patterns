from typing import List

def product_array_without_current_element(nums: List[int]) -> List[int]:
    size = len(nums)
    res = [1] * size
    for i in range(1, size):
        res[i] = res[i-1] * nums[i-1]

    right_running_pdt = 1
    for i in range(size-1, -1, -1):
        res[i] *= right_running_pdt
        right_running_pdt *= nums[i]
        
    return res