import heapq
class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD=10**9+7

        graph=[[] for _ in range(n)]

        for u,v,w in roads:
            graph[u].append((v,w))
            graph[v].append((u,w))

        dist=[float('inf')]*n
        ways=[0]*n

        pq=[(0,0)]
        dist[0]=0
        ways[0]=1

        while pq:
            time,node=heapq.heappop(pq)

            if time > dist[node]:
                continue
            for nei,t in graph[node]:
                if time+t<dist[nei]:
                    dist[nei]=time+t
                    ways[nei]=ways[node]
                    heapq.heappush(pq,(time+t,nei))
                elif time+t==dist[nei]:
                    ways[nei]=(ways[nei]+ways[node])%MOD
        return ways[n-1]%MOD

        