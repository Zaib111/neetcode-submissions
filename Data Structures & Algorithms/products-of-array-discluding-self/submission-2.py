class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zero_product=1
        zeros = 0
        for num in nums:
            product*=num
            if num != 0:
                zero_product *= num
            else:
                zeros += 1

        if 0 not in nums:
            return [product//num for num in nums]
        else:
            lst = []
            for i in range(len(nums)):
                if nums[i]!=0:
                    lst.append(0)
                else:
                    if zeros > 1:
                        lst.append(0)
                    else:
                        lst.append(zero_product)
            return lst