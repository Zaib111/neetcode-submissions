class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {}
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in res:
                return [res[difference], i]            
            res[nums[i]] = i