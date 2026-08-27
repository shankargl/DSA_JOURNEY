class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        q=deque()
        m=len(grid)
        n=len(grid[0])

        vis=[[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i==0 or j==0 or i==m-1 or j==n-1:
                    if grid[i][j]==1:
                        vis[i][j]=1
                        q.append((i,j))
        while q:
            r,c=q.popleft()
            dire=[(0,1),(0,-1),(1,0),(-1,0)]
            for dr,dc in dire:
                nr=r+dr
                nc=c+dc
                if 0<=nr<m and 0<=nc<n and vis[nr][nc]==0 and grid[nr][nc]==1:
                    vis[nr][nc]=1
                    q.append((nr,nc))

        count=0
        for k in range(m):
            for l in range(n):
                if grid[k][l]==1 and vis[k][l]==0:
                    count+=1
        return count