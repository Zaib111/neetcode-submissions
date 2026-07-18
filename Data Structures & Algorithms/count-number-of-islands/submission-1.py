class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        numIslands = 0
        rows, cols = len(grid), len(grid[0])
        visited = set()

        def bfs(r, c):
            q = deque()
            q.append((r, c))
            while q:
                r, c = q.pop()
                directions = [[0, 1], [0, -1], [-1, 0], [1, 0]]
                for dr, dc in directions:
                    new_r, new_c = r + dr, c + dc
                    if 0 <= new_r < rows and 0 <= new_c < cols and grid[new_r][new_c] == "1" and (new_r, new_c) not in visited:
                        visited.add((new_r, new_c))
                        q.append((new_r, new_c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    visited.add((r, c))
                    numIslands += 1
                    bfs(r, c)
        return numIslands
