class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_index = -1
        rows, cols = len(matrix) - 1, len(matrix[0]) - 1
        l, r = 0, rows
        while l <= r:
            m = (l + r) // 2
            if target > matrix[m][cols]:
                l = m + 1
            elif target < matrix[m][0]:
                r = m - 1
            else:
                row_index = m
                break
        if row_index == -1:
            return False
        l, r = 0, cols
        while l <= r:
            m = (l + r) // 2
            if target > matrix[row_index][m]:
                l = m + 1
            elif target < matrix[row_index][m]:
                r = m - 1
            else:
                return True
        return False