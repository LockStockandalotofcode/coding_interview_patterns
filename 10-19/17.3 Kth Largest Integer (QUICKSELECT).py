from typing import List
import random

def kth_largest_integer(nums: List[int], k: int) -> int:
    # QUICKSELECT
    if not nums:
        return 0
    
    result_index = quickselect(nums, 0, len(nums) - 1, k)
    return nums[result_index]

def quickselect(nums: List[int], left: int, right: int, k: int) -> int:
    if left >= right:
        return left
    n = len(nums)

    # randomising before choosing rightmost element as pivot
    random_idx = random.randint(left, right)
    nums[right], nums[random_idx] = nums[random_idx], nums[right]

    pivot_idx = partition(nums, left, right)
    if pivot_idx < n-k:
        return quickselect(nums, pivot_idx + 1, right, k)
    elif n-k < pivot_idx:
        return quickselect(nums, left, pivot_idx - 1, k)
    else:
        return pivot_idx

def partition(nums: List[int], left: int, right: int) -> int:
    pivot = nums[right]
    lo = left

    for i in range(left, right):
        if nums[i] < pivot:
            # swap lo, and this number
            nums[lo], nums[i] = nums[i], nums[lo]
            lo += 1
            
    # swap lo with pivot
    nums[lo], nums[right] = nums[right], nums[lo]
    return lo