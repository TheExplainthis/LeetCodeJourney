from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums.sort()
        longest_length = 1
        current_length = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                if nums[i] == nums[i - 1] + 1:
                    current_length += 1
                else:
                    longest_length = max(longest_length, current_length)
                    current_length = 1

        return max(longest_length, current_length)
