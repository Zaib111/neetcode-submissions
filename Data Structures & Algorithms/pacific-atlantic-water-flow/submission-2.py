class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # run bfs from pacific first to see all reachable cells and repeat for atlantic and take union
        rows, cols = len(heights), len(heights[0])
        pq = deque()
        aq = deque()
        for r in range(rows):
            pq.append((r, 0))
            aq.append((r, cols - 1))
        for c in range(cols):
            pq.append((0, c))
            aq.append((rows - 1, c))
        
        def bfs(q):
            res = []
            visited = set()
            while q:
                r, c = q.popleft()
                res.append([r, c])
                visited.add((r, c))
                directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if nr in range(rows) and nc in range(cols) and heights[nr][nc] >= heights[r][c] and (nr, nc) not in visited:
                        q.append((nr, nc))
        
            return res
        
        p_res, a_res = bfs(pq), bfs(aq)
        res = []
        for p in p_res:
            if p in a_res and p not in res:
                res.append(p)
        for a in a_res:
            if a in p_res and a not in res:
                res.append(a)
        return res