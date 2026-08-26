class Solution:
    def findCircleNum(self, num: List[List[int]]) -> int:
        def dfs(node,add_arr,visited):
            visited[node]=True
            for j in add_arr[node]:
                if not visited[j]:
                    dfs(j,add_arr,visited)
        
        n=len(num)
        m=len(num[0])
        add_arr=[[] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if num[i][j]==1 and i!=j:
                    add_arr[i].append(j)
                    add_arr[j].append(i)
        visited=[False]*n
        count=0
        for i in range(n):
            if not visited[i]:
                count+=1
                dfs(i,add_arr,visited)
        return count
        