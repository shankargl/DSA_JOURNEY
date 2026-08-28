class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        def topologicalSort(n, edges):

            graph = [[] for _ in range(n)]

            indegree = [0] * n

            for u, v in edges:
                graph[u].append(v)
                indegree[v] += 1

            
            q = deque()

            for i in range(n):
                if indegree[i] == 0:
                    q.append(i)

            ans = []

            
            while q:

                node = q.popleft()
                ans.append(node)

                for neighbor in graph[node]:

                    indegree[neighbor] -= 1

                    if indegree[neighbor] == 0:
                        q.append(neighbor)

            if len(ans) != n:
                return False

            return True
        return topologicalSort(numCourses, prerequisites)