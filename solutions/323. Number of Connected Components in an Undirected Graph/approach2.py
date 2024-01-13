class Solution:
    def countComponents(self, n, edges):
        parents = [i for i in range(n)]
        rank = [0] * n

        def find(vertex):
            if vertex == parents[vertex]:
                return vertex
            parents[vertex] = find(parents[vertex])
            return parents[vertex]

        def combine(vertex1, vertex2):
            vertex1 = find(vertex1)
            vertex2 = find(vertex2)

            if vertex1 == vertex2:
                return 0
            else:
                if rank[vertex1] > rank[vertex2]:
                    parents[vertex2] = vertex1
                elif rank[vertex1] < rank[vertex2]:
                    parents[vertex1] = vertex2
                else:
                    parents[vertex2] = vertex1
                    rank[vertex1] += 1
                return 1

        components = n
        for edge in edges:
            components -= combine(edge[0], edge[1])

        return components
