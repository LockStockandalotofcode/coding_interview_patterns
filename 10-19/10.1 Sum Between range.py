from typing import List

class SumBetweenRange:
    def __init__(self, nums: List[int]):
        self.prefix_sum = [0]
        for i in range(len(nums)):
            pre_sum = self.prefix_sum[-1] + nums[i]
            self.prefix_sum.append(pre_sum)

    def sum_range(self, i: int, j: int):
        return self.prefix_sum[j + 1] - self.prefix_sum[i]