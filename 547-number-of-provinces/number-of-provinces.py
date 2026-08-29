class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        m=len(isConnected)
        n=len(isConnected[0])
        def dfs(node,visited,add_list):
            visited[node]=1
            for nei in add_list[node]:
                if visited[nei]==0:
                    dfs(nei,visited,add_list)

        graph=[[] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if isConnected[i][j]==1 and i!=j:
                    graph[i].append(j)
                    graph[j].append(i)
        
        visited=[0]*m
        count=0
        for i in range(m):
            if visited[i]==0:
                count+=1
                dfs(i,visited,graph)
        return count
        
        