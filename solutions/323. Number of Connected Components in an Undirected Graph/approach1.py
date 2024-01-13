from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if n == 0:
            return 0

        components = 0
        visited = [0] * n
        graph = [[] for _ in range(n)]
        for edge in edges:
            node1, node2 = edge
            graph[node1].append(node2)
            graph[node2].append(node1)
        
        def dfs(node):
            visited[node] = 1
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    dfs(neighbor)

        for node in range(n):
            if visited[node] == 0:
                components += 1
                dfs(node)
        return components
