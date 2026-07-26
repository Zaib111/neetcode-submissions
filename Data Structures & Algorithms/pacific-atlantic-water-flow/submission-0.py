class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # run bfs twice: once from pacific end, once from atlantic end. if a node can be reached from both ends, it is good cell
        rows, cols = len(heights), len(heights[0])
        q = deque()
        res = []
        visited = set()

        # pacific
        for r in range(rows):
            q.append([r, 0])
            visited.add((r, 0))
        for c in range(1, cols):
            q.append([0, c])
            visited.add((0, c))
        
        while q:
            r, c = q.popleft()
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                if nr in range(rows) and nc in range(cols) and (nr, nc) not in visited and heights[nr][nc] >= heights[r][c]:
                    visited.add((nr, nc))
                    q.append([nr, nc])
        
        q = deque()
        # atlantic
        visited_atlantic = set()
        for r in range(rows):
            q.append([r, cols - 1])
            visited_atlantic.add((r, cols - 1))
        for c in range(0, cols - 1):
            q.append([rows - 1, c])
            visited_atlantic.add((rows - 1, c))
        while q:
            r, c = q.popleft()
            if (r, c) in visited: 
                res.append([r, c])
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                if nr in range(rows) and nc in range(cols) and (nr, nc) not in visited_atlantic and heights[nr][nc] >= heights[r][c]:
                    q.append([nr, nc])
                    visited_atlantic.add((nr, nc))
        
        return res