class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area_so_far = 0
        l, r = 0, len(heights) - 1
        while l < r:
            width = r - l
            height = min(heights[l], heights[r])
            max_area_so_far = max(width * height, max_area_so_far)
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return max_area_so_far