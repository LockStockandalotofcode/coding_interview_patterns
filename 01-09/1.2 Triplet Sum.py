from typing import List

def triplet_sum(nums: List[int]) -> List[List[int]]:
    if not nums or len(nums) < 3:
        return []

    triplets = []
    nums = sorted(nums)

    def pair_sum_sorted(nums_list: List[int], start: int, target: int):
        left = start
        right = len(nums_list) - 1
        pair_sum = []

        while left < right:
            curr_sum = nums_list[left] + nums_list[right]
            if curr_sum > target:
                right -= 1
            elif curr_sum < target:
                left += 1
            else:
                pair_sum.append([nums_list[left], nums_list[right]])
                left += 1

                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                right -= 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
        
        return pair_sum

    for i in range(len(nums) - 2):
        # skip duplicate for first anchor number
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        pairs = pair_sum_sorted(nums, i + 1, -nums[i])

        for pair in pairs:
            triplet = [nums[i]] + pair
            triplets.append(triplet)
    
    return triplets