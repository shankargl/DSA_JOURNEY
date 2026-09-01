import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = [[] for _ in range(n + 1)]

        for u, v, w in times:
            graph[u].append((v, w))

        pq = [(0, k)]

        dist = [float('inf')] * (n + 1)
        dist[k] = 0

        while pq:
            t, node = heapq.heappop(pq)
            if t>dist[node]:
                continue

            for nei, time in graph[node]:
                new = t + time

                if new < dist[nei]:
                    dist[nei] = new
                    heapq.heappush(pq, (new, nei))

        ans=max(dist[1:])
        if ans==float('inf'):
            return -1
        return ans