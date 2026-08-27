class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])

        def dfs(r, c, vis):
            vis[r][c] = 1

            dire = [(0, -1), (0, 1), (1, 0), (-1, 0)]

            for dr, dc in dire:
                nr = r + dr
                nc = c + dc

                if (0 <= nr < m and 
                    0 <= nc < n and 
                    vis[nr][nc] == 0 and 
                    board[nr][nc] == 'O'):
                    
                    dfs(nr, nc, vis)

        vis = [[0] * n for _ in range(m)]

        for i in range(n):
            if board[0][i] == 'O' and vis[0][i] == 0:
                dfs(0, i, vis)

            if board[m - 1][i] == 'O' and vis[m - 1][i] == 0:
                dfs(m - 1, i, vis)

       
        for j in range(m):
            if board[j][0] == 'O' and vis[j][0] == 0:
                dfs(j, 0, vis)

            if board[j][n - 1] == 'O' and vis[j][n - 1] == 0:
                dfs(j, n - 1, vis)

        for k in range(m):
            for l in range(n):
                if board[k][l] == 'O' and vis[k][l] == 0:
                    board[k][l] = 'X'