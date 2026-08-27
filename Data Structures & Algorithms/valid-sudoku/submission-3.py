class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            seen_rows = set()
            seen_cols = set()
            for j in range(9):
                if board[i][j] in seen_rows or board[j][i] in seen_cols: return False
                if board[i][j] != '.': seen_rows.add(board[i][j])
                if board[j][i] != '.': seen_cols.add(board[j][i])
            seen_rows, seen_cols = set(), set()
        
        res = defaultdict(set)
        for r in range(9):
            for c in range(9):
                if board[r][c] in res[(r // 3,  c // 3)]: return False
                if board[r][c] != '.': res[(r // 3, c // 3)].add(board[r][c])
        return True