from typing import List
import collections


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != (n - 1):
            return False

        graph = collections.defaultdict(list)
        for A, B in edges:
            graph[A].append(B)
            graph[B].append(A)
        
        visited = {0}
        queue = collections.deque([0])

        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if neighbor in visited:
                    continue
                visited.add(neighbor)
                queue.append(neighbor)
        return len(visited) == n
