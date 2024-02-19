from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last_position = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= last_position:
                last_position = i
        return last_position == 0
