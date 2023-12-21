import collections
import heapq
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_map = collections.defaultdict(int)
        for num in nums:
            frequency_map[num] += 1

        min_heap = [(-freq, num) for num, freq in frequency_map.items()]
        heapq.heapify(min_heap)

        top_k = [heapq.heappop(min_heap)[1] for _ in range(k)]
        return top_k
