from typing import List

def product_array_without_current_element(nums: List[int]) -> List[int]:
    size = len(nums)
    left_pdts, right_pdts, res = [1] * size, [1] * size, [1] * size
    for i in range(1, size):
        left_pdts[i] = left_pdts[i-1] * nums[i-1]

    for i in range(size-2, -1, -1):
        right_pdts[i] = right_pdts[i+1] * nums[i+1]
    
    for i in range(size):
        res[i] = left_pdts[i] * right_pdts[i]

    return res
