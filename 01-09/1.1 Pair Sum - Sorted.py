from typing import List

def pair_sum_sorted(nums: List[int], target: int) -> List[int]:
    left = 0
    right = len(nums) - 1

    res = []

    while left < right:
        curr_sum = nums[left] + nums[right]

        if curr_sum < target:
            left += 1
        elif curr_sum > target:
            right -= 1
        else:
            res.append(left)
            res.append(right)
            return res

    return res
