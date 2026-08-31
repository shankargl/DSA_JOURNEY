class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        if m==1 and n==1:
            if grid[0][0]==0:
                return 1
            else:
                return -1
        if grid[0][0] == 1 or grid[m-1][n-1] == 1:
            return -1

        dist=[[float('inf')]*n for _ in range(m)]
        dist[0][0]=1

        q=deque([(1,0,0)])

        dr = [-1,-1,-1,0,0,1,1,1]
        dc = [-1,0,1,-1,1,-1,0,1]

        while q:
            d,r,c=q.popleft()
            for i in range(8):
                nr=r+dr[i]
                nc=c+dc[i]
                if 0<=nr<m and 0<=nc<n and grid[nr][nc]==0 and d+1<dist[nr][nc]:
                    dist[nr][nc]=d+1
                    if (nr,nc)==(m-1,n-1):
                        return d+1
                    q.append((d+1,nr,nc))
        return -1