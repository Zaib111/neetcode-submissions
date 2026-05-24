class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapping={}
        for i in range(len(nums)):
            current = nums[i]
            #current + x = target so x = target - current
            difference = target - current
            if difference in mapping:
                return [mapping[difference],i]
            mapping[current] = i