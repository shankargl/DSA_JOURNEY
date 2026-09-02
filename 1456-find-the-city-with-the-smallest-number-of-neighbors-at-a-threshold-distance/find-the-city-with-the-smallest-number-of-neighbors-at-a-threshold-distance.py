class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        graph=[[float('inf')]*n for _ in range(n)]
        for i in range(n):
            graph[i][i]=0
        for u,v,w in edges:
            graph[u][v]=w
            graph[v][u]=w
        
        for k in range(n):
            for i in range(n):
                for j in range(n):

                    graph[i][j] = min(
                        graph[i][j],
                        graph[i][k] + graph[k][j]
                    )


        ans=-1
        min_count=n
        for i in range(n):
            count=0
            for j in range(n):
                if graph[i][j]<=distanceThreshold and i!=j:
                    count+=1
            if count<=min_count:
                min_count=count
                ans=i
        return ans
            