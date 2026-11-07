class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        rows, cols = len(grid), len(grid[0])
        seen = set()

        def bfs(r, c):
            q = deque()
            q.append((r, c))
            while q:
                r, c = q.popleft()
                seen.add((r, c))
                directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if nr in range(rows) and nc in range(cols) and grid[nr][nc] == "1" and (nr, nc) not in seen:
                        seen.add((nr, nc))
                        q.append((nr, nc))
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in seen:
                    res += 1
                    bfs(r, c)
        return res