class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        def bfs(q, r, c, visited):
            directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
            while q:
                r, c, dist = q.popleft()
                if grid[r][c] == 2**31 - 1: 
                    grid[r][c] = dist
                visited.add((r, c))
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if nr in range(rows) and nc in range(cols) and (nr, nc) not in visited and grid[nr][nc] != -1:
                        q.append((nr, nc, dist + 1))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0: q.append((r, c, 0))
        bfs(q, r, c, set())