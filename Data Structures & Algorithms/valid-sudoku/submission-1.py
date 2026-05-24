class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        count_row = set()
        for row in board:
            for element in row:
                if element in count_row:
                    return False
                if element != '.':
                    count_row.add(element)
            count_row = set()
        
        count_col = set()
        for i in range(9):
            for row in board:
                if row[i] in count_col:
                    return False
                if row[i] != '.':
                    count_col.add(row[i])
            count_col = set()
        
        count_box = defaultdict(set)
        for i in range(9):
            for j in range(9):
                if board[i][j] in count_box[(i//3, j//3)]:
                    return False
                if board[i][j] != '.':
                    count_box[(i//3, j//3)].add(board[i][j])
        
        return True