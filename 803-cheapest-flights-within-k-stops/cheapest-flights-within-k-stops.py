class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        adj = [[] for _ in range(n)]

        for u, v, w in flights:
            adj[u].append((v, w))

        q = deque([(0, src, 0)])  # stops, node, cost

        dist = [float('inf')] * n
        dist[src] = 0

        while q:
            stops, node, cost = q.popleft()

            if stops > k:
                continue

            for adjNode, edW in adj[node]:

                if cost + edW < dist[adjNode]:
                    dist[adjNode] = cost + edW

                    q.append(
                        (stops + 1, adjNode, cost + edW)
                    )

        if dist[dst] == float('inf'):
            return -1

        return dist[dst]
            