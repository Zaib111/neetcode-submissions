class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r: # <= since there could be an array with single element
            if nums[l] < nums[r]: # we've eliminated one of the sub arrays - we don't know which one, that's why we take the minimum.
                res = min(res, nums[l])
                break
            m = (l + r) // 2
            res = min(nums[m], res)
            if nums[m] >= nums[0]: # in the left subarray, the greater one
                l = m + 1
            else:
                r = m - 1
        
        return res