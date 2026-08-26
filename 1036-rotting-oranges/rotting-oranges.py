class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        m, n = len(grid), len(grid[0])

        rotten = deque()

        total = 0
        count = 0

        for i in range(m):
            for j in range(n):
            
                if grid[i][j] != 0:
                    total += 1

                if grid[i][j] == 2:
                    rotten.append((i, j))

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        days = 0

        # BFS loop
        while rotten:
            k = len(rotten)
            count += k

            for _ in range(k):
                x, y = rotten.popleft()

                for dx, dy in directions:
                    nx, ny = x + dx, y + dy

                    if nx < 0 or ny < 0 or nx >= m or ny >= n or grid[nx][ny] != 1:
                        continue

                    grid[nx][ny] = 2

                    rotten.append((nx, ny))

            if rotten:
                days += 1

        return days if count == total else -1

