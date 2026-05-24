class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l, r = 0, len(matrix) - 1
        
        while l < r:
            for i in range(r - l):
                t, b = l, r
                
                # save top left
                top_left = matrix[t][l + i]

                # move bottom left into top left
                matrix[t][l + i] = matrix[b - i][l]

                # move bottom right into bottom left
                matrix[b - i][l] = matrix[b][r - i]

                # move top right into bottom left
                matrix[b][r - i] = matrix[t + i][r]

                # move top left into bottom right
                matrix[t + i][r] = top_left
            l += 1
            r -= 1