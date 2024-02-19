from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda interval: interval[0])

        merged_intervals = []
        for current_interval in intervals:
            if not merged_intervals or merged_intervals[-1][1] < current_interval[0]:
                merged_intervals.append(current_interval)
            else:
                merged_intervals[-1][1] = max(merged_intervals[-1][1], current_interval[1])

        return merged_intervals
