class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []

        def dfs(r, cols, posDiag, negDiag, board):
            if r == n:
                res.append(board.copy())
                return
            for c in range(n):
                if not (c in cols or (r + c) in posDiag or (r - c) in negDiag):
                    cols.add(c)
                    posDiag.add((r + c))
                    negDiag.add((r - c))
                    s = ["."] * n
                    s[c] = "Q"
                    board.append("".join(s))
                    dfs(r + 1, cols, posDiag, negDiag, board)
                    cols.remove(c)
                    posDiag.remove((r + c))
                    negDiag.remove((r - c))
                    board.pop()
        dfs(0, set(), set(), set(), [])
        return res