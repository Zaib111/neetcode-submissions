class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_l, row_r = 0, len(matrix) - 1
        cols = len(matrix[0]) - 1
        row = -1;
        while row_l <= row_r:
            row_m = (row_l + row_r)//2
            if matrix[row_m][0] <= target <= matrix[row_m][cols]:
                row = row_m
                break
            elif target < matrix[row_m][0]:
                row_r = row_m - 1
            else:
                row_l = row_m + 1
        if row == -1:
            return False
        l, r = 0, cols
        while l <= r:
            m = (l + r) // 2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True
        return False