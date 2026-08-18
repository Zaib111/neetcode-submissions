class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curMax, curMin = 1, 1
        for num in nums:
            temp = num * curMin
            curMin = min(num * curMin, num * curMax, num)
            curMax = max(temp, num * curMax, num)
            res = max(res, curMax)
        return res