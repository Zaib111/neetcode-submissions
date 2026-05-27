class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # rows
        for i in range(9):
            seen = set()
            for j in range(9):
                if board[i][j] != '.':
                    if board[i][j] in seen:
                        return False
                    else:
                        seen.add(board[i][j])

        # cols
        for i in range(9):
            seen = set()
            for j in range(9):
                if board[j][i] != '.':
                    if board[j][i] in seen:
                        return False
                    else:
                        seen.add(board[j][i])
        
        # 3x3
        res = defaultdict(list)
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    coord = (i//3, j//3)
                    if coord in res and board[i][j] in res[coord]:
                        return False
                    else:
                        res[coord].append(board[i][j])
        
        return True