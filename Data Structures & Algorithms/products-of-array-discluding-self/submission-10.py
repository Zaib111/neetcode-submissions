class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #prefix and postfix arrays
        prefix, postfix = [0] * len(nums), [0] * len(nums)
        product = 1
        for i in range(len(nums)):
            prefix[i] = product
            product *= nums[i]
        product = 1
        for i in range(len(nums) - 1, -1, -1):
            postfix[i] = product
            product *= nums[i]
        res = []
        for i in range(len(nums)):
            res.append(prefix[i] * postfix[i])
        return res
