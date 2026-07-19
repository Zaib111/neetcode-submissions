class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        numIslands = 0
        visited = set()
        rows, cols = len(grid), len(grid[0])

        def bfs(r, c):
            q = deque()
            q.append((r, c))
            while q:
                r, c = q.popleft()
                visited.add((r, c))
                directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if nr in range(rows) and nc in range(cols) and (nr, nc) not in visited and grid[nr][nc] == "1":
                        visited.add((nr, nc))
                        q.append((nr, nc))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    numIslands += 1
                    bfs(r, c)
        return numIslands