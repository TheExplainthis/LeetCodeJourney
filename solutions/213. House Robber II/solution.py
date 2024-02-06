from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
    
        def solve(nums):
            first = second = 0
            for num in nums:
                first, second = second, max(second, first + num)
            return second
        return max(solve(nums[:-1]), solve(nums[1:]))
