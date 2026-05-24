class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, postfix, res = [], [], []
        for i in range(len(nums)):
            pre_product = 1
            for j in range(0, i):
                pre_product *= nums[j]
            post_product = 1
            for j in range(i + 1, len(nums)):
                post_product *= nums[j]
            prefix.append(pre_product)
            postfix.append(post_product)
            res.append(prefix[i] * postfix[i])
        return res