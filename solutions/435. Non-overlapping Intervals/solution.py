from typing import List
import math

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[1])
        ans = 0
        last_end = -math.inf
        
        for start_i, end_i in intervals:
            if start_i >= last_end:
                last_end = end_i
            else:
                ans += 1
        return ans
