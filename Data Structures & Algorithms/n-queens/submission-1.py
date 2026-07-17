class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []

        def dfs(r, cols, negDiag, posDiag, board):
            if r == n:
                res.append(board.copy())
                return
            for c in range(n):
                if c not in cols and (r - c) not in negDiag and (r + c) not in posDiag:
                    cols.add(c)
                    negDiag.add((r - c))
                    posDiag.add((r + c))
                    s = ["."] * n
                    s[c] = "Q"
                    board.append("".join(s))
                    dfs(r + 1, cols, negDiag, posDiag, board)
                    cols.remove(c)
                    negDiag.remove((r - c))
                    posDiag.remove((r + c))
                    board.pop()
        dfs(0, set(), set(), set(), [])
        return res