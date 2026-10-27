class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        grid=[['#']*n for _ in range(m)]

        for i in range(n):
            grid[0][i]='.'
        for j in range(m):
            grid[j][n-1]='.'

        print(grid)
        ans=[]
        for i in grid:
            ans.append("".join(i))
        
        return ans