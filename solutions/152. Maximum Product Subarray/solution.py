from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        max_prod = min_prod = ans = nums[0]
        
        for i in range(1, len(nums)):
            num = nums[i]
            if num < 0:
                max_prod, min_prod = min_prod, max_prod
            max_prod = max(num, max_prod * num)
            min_prod = min(num, min_prod * num)
            ans = max(ans, max_prod)
        return ans
