from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        slow, fast = 0, 0
        
        while fast < len(prices):
            current_profit = prices[fast] - prices[slow]
            max_profit = max(max_profit, current_profit)
            if prices[slow] > prices[fast]:
                slow = fast
            fast += 1
        return max_profit
