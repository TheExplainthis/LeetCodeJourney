from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []

        for i, (start_i, end_i) in enumerate(intervals):
            if end_i < newInterval[0]:
                result.append([start_i, end_i])
            elif newInterval[1] < start_i:
                result.append(newInterval)
                newInterval = [start_i, end_i]
            else:
                newInterval[0] = min(newInterval[0], start_i)
                newInterval[1] = max(newInterval[1], end_i)
        result.append(newInterval)
        return result
