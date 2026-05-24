class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapping={}
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in mapping:
                return [mapping[difference], i]
            mapping[nums[i]] = i