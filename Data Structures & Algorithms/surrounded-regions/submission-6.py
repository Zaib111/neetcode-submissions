class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        visited = set()
        q = deque()
        # run bfs from the edge to see all O's that are reachable and thus "not surrounded"

        def bfs():
            while q:
                r, c = q.popleft()
                visited.add((r, c))
                board[r][c] = "Not Surrounded"
                dirs = [[0, 1], [1, 0], [-1, 0], [0, -1]]
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if nr in range(rows) and nc in range(cols) and board[nr][nc] == "O" and (nr, nc) not in visited:
                        visited.add((nr, nc))
                        q.append((nr, nc))

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and (r in {0, rows - 1} or c in {0, cols - 1}):
                    q.append((r, c))
        bfs()
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "Not Surrounded":
                    board[r][c] = "O"
        