class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.res = 0
        rows, cols = len(grid), len(grid[0])
        seen = set()

        def bfs(r, c):
            q = deque()
            q.append((r, c))
            cur_area = 0
            while q:
                r, c = q.popleft()
                seen.add((r, c))
                cur_area += 1
                self.res = max(self.res, cur_area)
                directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if nr in range(rows) and nc in range(cols) and (nr, nc) not in seen and grid[nr][nc] == 1:
                        q.append((nr, nc))
                        seen.add((nr, nc))
        
        for r in range(rows):
            for c in range(cols):
                if (r, c) not in seen and grid[r][c] == 1:
                    bfs(r, c)
        return self.res