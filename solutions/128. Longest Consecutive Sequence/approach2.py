from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_length = 0
        nums_set = set(nums)

        for left in nums_set:
            if left - 1 not in nums_set:
                right = left
                while right + 1 in nums_set:
                    right += 1
                longest_length = max(longest_length, right - left + 1)
        return longest_length