class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        nums = set(nums)
        for num in nums:
            if num - 1 not in nums:
                counter = 0
                while counter + num in nums:
                    counter += 1
                    res = max(res, counter)
        return res
            