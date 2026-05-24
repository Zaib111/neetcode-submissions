class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return not len({num for num in nums}) == len(nums)