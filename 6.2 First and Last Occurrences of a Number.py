from typing import List

def first_and_last_occurrences_of_a_number(nums: List[int], target: int) -> int:
    lower_bound = lower_bound_binary_search(nums, target)
    upper_bound = upper_bound_binary_search(nums, target)
    
    return [lower_bound, upper_bound]


def lower_bound_binary_search(nums: int, target: int) -> int:
    # lower bound binary search
    # if mid <, shrink to right, move left , excluding mid
    # if mid =, shrink to left, move right, include mid
    # if mid >, shrink to left, move right, exclude mid
    left, right = 0, len(nums) - 1

    while left < right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] == target:
            right = mid
        else:
            right = mid - 1
        
    return left if nums and  nums[left] == target else -1

def upper_bound_binary_search(nums: int, target: int) -> int:
    # upper bound binary seach
    # if mid <, shrink to right, move left , excluding mid
    # if mid =, shrink to right, move left, include mid
    # if mid >, shrink to left, move right, exclude mid
    # calculate mid with right bias
    left, right = 0, len(nums) - 1

    while left < right:
        mid = (left + right) // 2 + 1
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] == target:
            left = mid
        else:
            right = mid - 1
    return right if nums and  nums[right] == target else -1