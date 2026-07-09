from typing import List
from random import randint

def sort_array(nums: List[int]) -> List[int]:
    # choose pivot, put elements leess than pivot to its left
    # then resursively sort the left and right parts of this pivot
    quicksort(nums, 0, len(nums) - 1)
    return nums

def quicksort(nums: List[int], left: int, right: int) -> None:
    # base case - 0 or 1 elements
    if left >= right:
        return 
    # partition and arrange as per pivot
    # to avoid extreme pivots
    random_idx = randint(left, right)
    # swap with rightmost element
    nums[right], nums[random_idx] = nums[random_idx], nums[right]
    
    # then recurse on left and right subarrays
    pivot_idx = partition(nums, left, right)

    # recurse on sub arrays
    quicksort(nums, left, pivot_idx - 1)
    quicksort(nums, pivot_idx + 1, right)

def partition(nums: List[int], left: int, right: int) -> int:
    # rightmost element as the pivot for the moment
    pivot = nums[right]
    lo = left

    # arranging elements as per pivot
    for i in range(left, right):
        if nums[i] < pivot:
            nums[lo], nums[i] = nums[i], nums[lo]
            lo += 1
    
    # now lo is where pivot must lie
    nums[right], nums[lo] = nums[lo], nums[right]
    return lo