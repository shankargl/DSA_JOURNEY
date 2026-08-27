class Solution:
    def highestPeak(self, mat: List[List[int]]) -> List[List[int]]:
        m=len(mat)
        n=len(mat[0])
        visited=[[0]*n for _ in range(m) ]
        new=[[0]*n for _ in range(m)]
        q=deque()
        for i in range(m):
            for j in range(n):
                if mat[i][j]==1:
                    visited[i][j]=1
                    q.append((i,j,0))
        while  q:
            dire=[(0,1),(0,-1),(1,0),(-1,0)]
            for _ in range(len(q)):  
                r,c,d=q.popleft()
                new[r][c]=d
                for dr,dc in dire:
                    nr=r+dr
                    nc=c+dc
                    if 0<=nr<m and 0<=nc<n and visited[nr][nc]==0:
                        visited[nr][nc]=1
                        q.append((nr,nc,d+1))
        return new
