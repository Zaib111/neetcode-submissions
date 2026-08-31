class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        i = 0

        while i < len(nums):
            while i < len(nums) and i > 0 and nums[i] == nums[i - 1]:
                if i != len(nums) - 1:
                    i += 1
                else: break
            target = -1 * nums[i]
            l, r = i + 1, len(nums) - 1
            while l < r:
                cur = nums[l] + nums[r]
                if cur < target:
                    l += 1
                elif cur > target:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
            i += 1
        return res
        # [-1,0,1,2,-1,-4]
        # [-4,-1,-1,0,1,2]