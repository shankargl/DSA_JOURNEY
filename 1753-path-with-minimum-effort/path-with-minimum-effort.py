import heapq
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m=len(heights)
        n=len(heights[0])

        dist=[[float('inf')]*n for _ in range(m)]
        
        dist[0][0]=0
        pq=[(0,0,0)]
        
        while pq:
            d,r,c=heapq.heappop(pq)
            if r==m-1 and c==n-1:
                return d
            dire=[(1,0),(-1,0),(0,1),(0,-1)]
            for dr,dc in dire:
                nr=r+dr
                nc=c+dc
                if 0<=nr<m and 0<=nc<n:
                    new=max(d,abs(heights[r][c]-heights[nr][nc]))
                    if new<dist[nr][nc]:
                        dist[nr][nc]=new
                        heapq.heappush(pq,(new,nr,nc))
        return 0
