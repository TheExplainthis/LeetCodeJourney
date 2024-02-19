from typing import List
import heapq


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        meeting_end_times = []
        intervals.sort(key=lambda meeting: meeting[0])
        heapq.heappush(meeting_end_times, intervals[0][1])

        for start, end in intervals[1:]:
            if meeting_end_times[0] <= start:
                heapq.heappop(meeting_end_times)
            heapq.heappush(meeting_end_times, end)
        return len(meeting_end_times)
