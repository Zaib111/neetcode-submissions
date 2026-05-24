class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_product = [1] * len(nums)
        right_product = [1] * len(nums)
        res = []
        product = 1
        final_product = 1
        for num in nums:
            final_product *= num
        for i in range(len(nums)):
            if i != 0:
                left_product[i] = product
            product *= nums[i]
        product = 1
        for i in range(len(nums) - 1, -1, -1):
            if i != len(nums) - 1:
                right_product[i] = product
            product*=nums[i]
        for i in range(len(nums)):
            res.append(left_product[i] * right_product[i])
        return res
