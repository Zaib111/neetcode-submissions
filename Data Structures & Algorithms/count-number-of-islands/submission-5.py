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
                if grid[r][c] == "1" and (r, c) not in seen:
                    seen.add((r, c))
                    for i in {1, -1}:
                        if r + i in range(rows):
                            q.append((r + i, c))
                        if c + i in range(cols):
                            q.append((r, c + i))
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in seen:
                    res += 1
                    bfs(r, c)
        return res