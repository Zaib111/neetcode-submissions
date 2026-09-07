class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums) - 1
        while l <= r:
            if nums[l] <= nums[r]:
                return min(res, nums[l])
                
            m = (l + r) // 2
            if nums[m] >= nums[r]: # larger/left portion
                l = m + 1 # search right to go to smaller/right portion
            else: # smaller/right portion
                r = m - 1 # move left to find min in smaller/right portion
                res = min(res, nums[m])