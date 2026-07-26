class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        q = deque()

        def bfs():
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            while q:
                r, c = q.popleft()
                board[r][c] = "#"
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if nr in range(rows) and nc in range(cols) and board[nr][nc] == "O":
                        q.append((nr, nc))

        for r in range(rows):
            if board[r][0] == "O":
                q.append((r, 0))
                bfs()
            if board[r][cols - 1] == "O":
                q.append((r, cols - 1))
                bfs()
        for c in range(cols):
            if board[0][c] == "O":
                q.append((0, c))
                bfs()
            if board[rows - 1][c] == "O":
                q.append((rows - 1, c))
                bfs()
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "#":
                    board[r][c] = "O"
                elif board[r][c] == "O":
                    board[r][c] = "X"