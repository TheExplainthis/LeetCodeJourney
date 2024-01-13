from collections import defaultdict, deque


class Solution:
    def canFinish(self, numCourses, prerequisites):
        indegree = defaultdict(int)
        graph = defaultdict(list)

        for (shoot_in, shoot_out) in prerequisites:
            graph[shoot_out].append(shoot_in)
            indegree[shoot_in] += 1

        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        visited_count = 0
        while queue:
            node = queue.popleft()
            visited_count += 1

            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        return visited_count == numCourses
