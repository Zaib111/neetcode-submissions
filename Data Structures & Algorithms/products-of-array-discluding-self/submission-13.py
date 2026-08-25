class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        prefix, postfix = nums[0], nums[-1]
        for i in range(1, len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        for i in range(len(nums) - 2, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res