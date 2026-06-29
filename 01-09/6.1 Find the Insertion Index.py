from typing import List

def find_the_insertion_index(nums: List[int], target: int) -> int:
    # BINARY SEARCH
    # TARGET - TO FIND NUMBER >= TARGET
    # MID VALUE > TARGET
    # SHRINK TO LEFT, INCLUDE MID, move right to mid
    
    # MID VALUE < TARGET
    # SHRINK TO RIGHT, EXCLUDE MID, move left to mid + 1

    # MID VALUE = TARGET, RETURN

    # when LEFT MEETS RIGHT, IT IS EITHER WHERE TARGET LIES OR IS TO BE INSERTED

    # since it could be n where target needs to be inserted, right starts from n, not n - 1
    left, right = 0, len(nums)

    while left < right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        if nums[mid] >= target:
            right = mid

    return left