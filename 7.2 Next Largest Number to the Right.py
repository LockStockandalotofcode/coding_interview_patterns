from typing import List

def next_largest_number_to_the_right(nums: List[int]) -> List[int]:
    stack = []
    res = [0] * len(nums)

    for i in range(len(nums) - 1, -1, -1):
        num = nums[i]
        while stack and stack[-1] <= num:
            stack.pop()
        
        res[i] = stack[-1] if stack else -1
        stack.append(num)
    
    return res
